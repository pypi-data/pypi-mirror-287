import typing

from firecore.import_utils import require
import functools
from pydantic import BaseModel, TypeAdapter
from loguru import logger


ConfigType = typing.Dict[str, typing.Dict[str, typing.Any]]
_config_adapter =TypeAdapter(ConfigType)

class ObjectPool:
    def __init__(self, config: ConfigType) -> None:
        self._config = _config_adapter.validate_python(config)
        self._pool: typing.Dict[str, typing.Any] = {}

    def get(self, key: str):
        """
        Args:
            key: key in config
        Returns:
            singleton
        """
        if key not in self._config:
            raise Exception(f"{key} not in config with keys {self._config.keys()}")

        if key not in self._pool:
            value = self._instantiate(self._config[key])
            self._pool[key] = value

        return self._pool[key]

    def _instantiate(self, config: typing.Any):
        if isinstance(config, dict):
            if "_type" in config:
                return self._instantiate_dict(config)
            else:
                return {k: self._instantiate(v) for k, v in config.items()}
        elif isinstance(config, list):
            return [self._instantiate(x) for x in config]
        elif isinstance(config, str):
            if config.startswith("ref:"):
                return self.get(config.split(":")[1])
            elif config.startswith("import:"):
                return require(config.split(":")[1])
        else:
            return config

    def _instantiate_dict(self, config: dict):
        _type: str = config["_type"]
        if _type in self._pool:
            logger.debug(f"reuse {_type}")
            return self._pool[_type]

        kwargs = {}
        for key, value in config.items():
            if key == "_type":
                continue
            kwargs[key] = self._instantiate(value)

        out = None
        if _type.startswith("call:"):
            out = require(_type.split(":")[1])(**kwargs)
        elif _type.startswith("partial:"):
            out = functools.partial(require(_type.split(":")[1]), **kwargs)

        self._pool[_type] = out
        return out


def _test():
    config = {
        "linear": {
            "_type": "call:torch.nn.Linear",
            "in_features": 2,
            "out_features": 4,
        },
        "dp": {"_type": "call:torch.nn.DataParallel", "module": "ref:linear"},
    }

    object_pool = ObjectPool(config)
    print(object_pool.get("linear"))
    print(object_pool.get("dp").module is object_pool.get('linear'))


if __name__ == "__main__":
    _test()
