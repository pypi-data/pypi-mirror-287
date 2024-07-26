import json
import traceback
from typing import Collection, Union

import MySQLdb
from django.conf import settings
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from opentelemetry.instrumentation.celery import CeleryInstrumentor
from opentelemetry.instrumentation.dbapi import (
    DatabaseApiIntegration,
    trace_integration,
)
from opentelemetry.instrumentation.django import DjangoInstrumentor
from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor
from opentelemetry.instrumentation.instrumentor import BaseInstrumentor
from opentelemetry.instrumentation.logging import LoggingInstrumentor
from opentelemetry.instrumentation.redis import RedisInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.trace import Span, Status, StatusCode, format_trace_id
from requests import Response

from ovinc_client.core.logger import logger
from ovinc_client.trace.constants import SPAN_DB_TYPE, SPAN_REDIS_TYPE, SpanAttributes


def requests_callback(span: Span, response: Union[Response, HttpResponse]):
    """
    Http Request Callback
    """

    # Set Status Code
    status_code = response.status_code
    span.set_attribute("statusCode", status_code)

    # Set Status
    if status_code < 300:
        span.set_status(Status(StatusCode.OK))
    else:
        span.set_status(Status(StatusCode.ERROR))


def django_request_hook(span: Span, request: WSGIRequest):
    """
    Django Request Hook
    """

    # Set Trace ID for Request
    trace_id = span.get_span_context().trace_id
    request.otel_trace_id = format_trace_id(trace_id)


def django_response_hook(span: Span, request: WSGIRequest, response: HttpResponse):
    """
    Django Response Hook
    """

    # Loads Response Content as Json
    try:
        result = json.loads(response.content)
        if not isinstance(result, dict):
            return
    except Exception:  # pylint: disable=W0718
        return

    # Set Attributes
    span.set_attribute(SpanAttributes.RESULT_MESSAGE, result.get("message", ""))
    span.set_attribute(SpanAttributes.RESULT_ERRORS, result.get("errors", ""))

    # Set Status
    requests_callback(span, response)


class DBApiIntegration(DatabaseApiIntegration):
    """
    DB Integration
    """

    def get_connection_attributes(self, connection):
        """
        Get Connection Params
        """

        try:
            host_info = str(connection.get_host_info())
            for conn in settings.DATABASES.values():
                if host_info.find(conn["HOST"]) != -1:
                    self.span_attributes[SpanAttributes.DB_INSTANCE] = conn["NAME"]
                    self.span_attributes[SpanAttributes.DB_NAME] = conn["NAME"]
                    self.span_attributes[SpanAttributes.DB_USER] = conn["USER"]
                    self.span_attributes[SpanAttributes.DB_TYPE] = SPAN_DB_TYPE
                    self.span_attributes[SpanAttributes.DB_PORT] = conn["PORT"]
                    self.span_attributes[SpanAttributes.DB_IP] = conn["HOST"]
                    break
        except Exception:  # pylint: disable=W0718
            logger.error(traceback.format_exc())


class RedisRequestHook:
    """
    Redis Request Hook
    """

    def __call__(self, span, instance, args, kwargs):
        span.set_attributes(
            {
                SpanAttributes.DB_INSTANCE: f"{SPAN_REDIS_TYPE}({settings.REDIS_DB})",
                SpanAttributes.DB_NAME: f"{SPAN_REDIS_TYPE}({settings.REDIS_DB})",
                SpanAttributes.DB_TYPE: SPAN_REDIS_TYPE,
                SpanAttributes.DB_PORT: settings.REDIS_PORT,
                SpanAttributes.DB_IP: settings.REDIS_HOST,
            }
        )


class Instrumentor(BaseInstrumentor):
    """
    Instrument OT
    """

    def instrumentation_dependencies(self) -> Collection[str]:
        return []

    def _instrument(self, **kwargs):
        LoggingInstrumentor().instrument()
        RequestsInstrumentor().instrument(span_callback=requests_callback)
        DjangoInstrumentor().instrument(request_hook=django_request_hook, response_hook=django_response_hook)
        CeleryInstrumentor().instrument()
        RedisInstrumentor().instrument(request_hook=RedisRequestHook())
        HTTPXClientInstrumentor().instrument()
        trace_integration(MySQLdb, "connect", "mysql", db_api_integration_factory=DBApiIntegration)

    def _uninstrument(self, **kwargs):
        if getattr(self, "instrumentors", None) is None:
            return
        for instrumentor in self.instrumentors:  # pylint: disable=E1101
            instrumentor.uninstrument()
