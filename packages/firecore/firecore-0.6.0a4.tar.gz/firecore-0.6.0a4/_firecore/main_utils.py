from typing import Callable, Optional, TypeVar, Union
import inspect
from .import_utils import require

T = TypeVar('T')


def _main_fn(func: T) -> T:
    # 拿到调用这个函数的 FrameInfo
    caller = inspect.stack()[2]
    # import ipdb; ipdb.set_trace()
    # 拿到 __name__
    name = caller.frame.f_globals['__name__']

    if name == '__main__':
        func()
    else:
        return func


def main_fn(func: Optional[T]) -> Union[Callable[[T], T], T]:
    if func:
        return _main_fn(func)
    else:
        return _main_fn
