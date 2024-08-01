from concurrent.futures import ThreadPoolExecutor
from opentelemetry import context as otel_context
from opentelemetry.sdk.trace import Tracer
from opentelemetry import trace as trace_api
from typing import Callable


class TracedThreadPoolExecutor(ThreadPoolExecutor):
    """Implementation of :class:`ThreadPoolExecutor` that will pass context into sub tasks."""

    def __init__(self, name: str, *args, **kwargs):
        tracer = trace_api.get_tracer(name)
        self.tracer = tracer
        super().__init__(*args, **kwargs)

    def with_otel_context(self, context: otel_context.Context, fn: Callable):
        otel_context.attach(context)
        return fn()

    def submit(self, fn, *args, **kwargs):
        """Submit a new task to the thread pool."""

        # get the current otel context
        context = otel_context.get_current()
        if context:
            return super().submit(
                lambda: self.with_otel_context(context, lambda: fn(*args, **kwargs)),
            )
        else:
            return super().submit(lambda: fn(*args, **kwargs))
