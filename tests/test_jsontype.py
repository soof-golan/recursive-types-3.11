from __future__ import annotations
from typing import TypeAlias
import pytest

Primitive: TypeAlias = str | int | float | bool | None
Json: TypeAlias = Primitive | list["Json"] | dict[str, "Json"]
JsonObject: TypeAlias = dict[str, Json]
JsonArray: TypeAlias = list[Json]


@pytest.mark.filterwarnings("error:.*")
def test_jsontype() -> None:
    obj: Json = {
        "my": "object",
        "deep": {
            "nested": "object",
            "A": [1, 2, 3]
        }
    }

