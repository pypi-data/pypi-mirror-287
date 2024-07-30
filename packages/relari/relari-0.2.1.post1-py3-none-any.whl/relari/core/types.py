from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, TypedDict, Union, Tuple
from math import isclose
UID = str


def args_to_dict(*args, **kwargs):
    arg_dict = dict(kwargs)
    for index, value in enumerate(args):
        arg_dict[f"_arg{index}"] = value
    return arg_dict


class ToolCall(TypedDict):
    name: str
    kwargs: Dict[str, Any]


class HTTPMethod(str, Enum):
    GET = "get"
    POST = "post"
    PUT = "put"
    DELETE = "delete"


@dataclass(frozen=True, eq=True)
class DatasetDatum:
    label: str
    data: dict

    def asdict(self):
        return {
            "label": self.label,
            "data": self.data,
        }


MetricsArgs = Union[DatasetDatum, Dict[str, Any]]

######################################################################################


@dataclass
class UserPrompt:
    prompt: str
    description: str

    def asdict(self):
        return {"prompt": self.prompt, "description": self.description}


@dataclass
class PromptOptimizationSettings:
    early_stopping_steps: int
    early_stopping_threshold: float
    num_epochs: int
    batch_size: int
    split_ratios: Tuple[float, float, float]

    @classmethod
    def defaults(cls):
        return cls(
            early_stopping_steps=3,
            early_stopping_threshold=1e-2,
            num_epochs=3,
            batch_size=5,
            split_ratios=(0.2, 0.4, 0.4),
        )

    def is_valid(self):
        assert self.early_stopping_steps > 0, "early_stopping_steps must be greater than 0"
        assert self.early_stopping_threshold > 0, "early_stopping_threshold must be greater than 0"
        assert self.num_epochs > 0, "num_epochs must be greater than 0"
        assert self.batch_size > 0, "batch_size must be greater than 0"
        assert isclose(sum(self.split_ratios), 1.0, rel_tol=1e-6) == 1, "split_ratios must sum to 1"
        return True

    def asdict(self):
        return {
            "early_stopping_steps": self.early_stopping_steps,
            "early_stopping_threshold": self.early_stopping_threshold,
            "num_epochs": self.num_epochs,
            "batch_size": self.batch_size,
            "split_ratios": self.split_ratios,
        }


@dataclass
class Prompt:
    system: str
    user: UserPrompt

    def is_valid(self):
        assert isinstance(self.user, UserPrompt), "user must be an instance of UserPrompt"
        assert self.system, "fixed must not be empty"
        assert self.user.prompt, "user.prompt must not be empty"
        assert self.user.description, "user.description must not be empty"
        return True


    def asdict(self):
        return {"system": self.system, "user": self.user.asdict()}
