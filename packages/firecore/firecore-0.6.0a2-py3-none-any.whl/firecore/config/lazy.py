from typing import TypeVar, TypedDict, Literal
from loguru import logger
import importlib
import functools
import importlib.util


@functools.lru_cache(maxsize=128)
def require(name: str):
    """
    import anything by name
    """
    module_name, _sep, attribute_name = name.rpartition(".")
    module = importlib.import_module(module_name)
    attribute = getattr(module, attribute_name)
    logger.debug("import {} from {}", attribute_name, module_name)
    return attribute


class LazyNode(TypedDict):
    _path_: str
    _type_: Literal["call", "import", "partial"]


def _get_target_path(target):
    return target.__module__ + "." + target.__name__


T = TypeVar("T")


def LazyCall(target: T) -> T:
    def f(**kwargs):
        return LazyNode(_path_=_get_target_path(target), _type_="call", **kwargs)

    return f


def LazyPartial(target: T) -> T:
    def f(**kwargs):
        return LazyNode(_path_=_get_target_path(target), _type_="partial", **kwargs)

    return f


def LazyImport(target: T):
    return LazyNode(_path_=_get_target_path(target), _type_="import")


def _instantiate_dict(config: dict):
    if "_path_" in config and "_type_" in config:
        target = require(config["_path_"])
        config_type = config["_type_"]

        if config_type == "import":
            return target

        kwargs = {
            k: instantiate(v)
            for k, v in config.items()
            if k not in ["_path_", "_type_"]
        }
        if config_type == "call":
            return target(**kwargs)
        elif config_type == "partial":
            return functools.partial(target, **kwargs)
    else:
        return {k: instantiate(v) for k, v in config.items()}


def instantiate(config):
    if isinstance(config, dict):
        return _instantiate_dict(config)
    elif isinstance(config, list):
        return [instantiate(x) for x in config]
    elif isinstance(config, tuple):
        return tuple(instantiate(x) for x in config)
    else:
        return config


def _is_lazy_config(x):
    return isinstance(x, dict) and "_path_" in x and "_type_" in x


def main():
    from firecore.opencv import decode_rgb_image
    from firecore.params import AllParams

    print(LazyCall(decode_rgb_image)(buf="123", c=1))


if __name__ == "__main__":
    main()
