from ddtrace import patch_all, tracer

patch_all()

import typing
from azure.functions import AppExtensionBase, Context
from logging import Logger

class TracerExtension(AppExtensionBase):
    """A Python worker extension to start Datadog tracer and insturment Azure Functions"""

    @classmethod
    def init(cls):
        print("============= new verison 14 ===========")
        pass

    @classmethod
    def pre_invocation_app_level(cls, context: Context, *args, **kwargs) -> None:
        print("here")
        print("context name: ", context.function_name)
        # logger.info("context: ", context)
        print("here1")
        # logger.info(f'Recording start time of {context.function_name}')
        # logger.info("context: ", context.function_name)

        func_name = context.function_name

        t = tracer.trace("azure.function")
        print("here3")

        span = tracer.current_span()
        print("span?: ", span)
        span.set_tag('route_name', func_name)
        print("span get tags: ==", span.get_tags())
        print("span after: ", span)
        print("trace ater: " , t)
        print("here4")
        cls.t = t
        print("here5")


    @classmethod
    def post_invocation_app_level(cls, *args, **kwargs) -> None:
        cls.t.finish()
        print("end")
        pass
