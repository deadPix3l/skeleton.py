from typing import Self
import yaml
from pydantic import BaseModel
from pathlib import Path

# a BaseModel that can be parsed from yaml
class YamlModel(BaseModel):
    @classmethod
    def from_yaml(
        cls,
        content: Path | str,
        *,
        as_string: bool = False,
        encoding: str = "utf-8",
        **kwargs,
    ) -> Self:
        content = str(content) if as_string else Path(content).read_text(encoding=encoding)
        return cls.model_validate_yaml(content, **kwargs)

    @classmethod
    def model_validate_yaml(
        cls,
        yaml_data: str | bytes,
        **kwargs
    ) -> Self:
        return cls.model_validate(yaml.safe_load(yaml_data), **kwargs)

