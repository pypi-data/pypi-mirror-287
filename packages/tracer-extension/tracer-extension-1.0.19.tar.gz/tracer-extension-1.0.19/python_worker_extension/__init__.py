from ddtrace import patch_all, tracer

patch_all()

from azure.functions import AppExtensionBase, Context

class TracerExtension(AppExtensionBase):
    """A Python worker extension to start Datadog tracer and insturment Azure Functions"""

    @classmethod
    def init(cls):
        print("============= new verison 9 ===========")
        # print("here0")
        # t = tracer.trace("azure.function")
        # print("here0.5")
        # span = tracer.current_span()
        # print("span?: ", span)
        # span.set_tag('function-name', 'ab')
        # span.set_struct_tag('function-name', 'ab')
        # print("tags on span: " , span.get_tags())
        # print("span after: ", span)
        # print("trace ater: " , t)
        pass

    @classmethod
    def pre_invocation_app_level(cls,context: Context, *args, **kwargs) -> None:
    # def pre_invocation_app_level(cls, *args, **kwargs) -> None:
        print("here")
        # func_name = context.function_name
        print("here1")

        t = tracer.trace("azure.function")
        print("here3")

        span = tracer.current_span()
        print("span?: ", span)
        # span.set_tag('function-name', f'{func_name}')
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
