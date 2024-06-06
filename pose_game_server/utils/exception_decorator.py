import inspect
from functools import wraps
from pydantic import ValidationError

from utils.exceptions import AppException

def handle_exceptions(func):
    @wraps(func)
    async def async_wrapper(*args, **kwargs):
        if len(args) > 0 and args[0] is not None and inspect.isclass(args[0]):
            class_name = args[0].__name__
            method_name = func.__name__
        else:
            class_name = func.__self__.__class__.__name__
            method_name = func.__name__
        try:
            return await func(*args, **kwargs)
        except AppException as ex:
            raise ex
        except ValidationError as ex:
            raise ex
        except Exception as ex:
            error_msg = f"{class_name}.{method_name}: {str(ex)}"
            raise AppException(message=error_msg)

    @wraps(func)
    def sync_wrapper(*args, **kwargs):
        if len(args) > 0 and args[0] is not None and inspect.isclass(args[0]):
            class_name = args[0].__name__
            method_name = func.__name__
        else:
            class_name = func.__self__.__class__.__name__
            method_name = func.__name__
        try:
            return func(*args, **kwargs)
        except AppException as ex:
            raise ex
        except ValidationError as ex:
            raise ex
        except Exception as ex:
            error_msg = f"{class_name}.{method_name}: {str(ex)}"
            raise AppException(message=error_msg)

    if inspect.iscoroutinefunction(func):
        return async_wrapper
    else:
        return sync_wrapper

def dec_each_method(decorator):
    def decorate(cls):
        for attr in cls.__dict__:
            obj = getattr(cls, attr)
            if callable(obj):
                setattr(cls, attr, decorator(obj))
        return cls
    return decorate