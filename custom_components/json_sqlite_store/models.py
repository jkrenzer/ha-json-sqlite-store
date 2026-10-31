"""Typed models used by the bootstrap integration scaffold."""

from __future__ import annotations

from dataclasses import dataclass

from homeassistant.config_entries import ConfigEntry
from pydantic import BaseModel, ConfigDict, Field

type JsonNativeValue = (
    None
    | bool
    | int
    | float
    | str
    | list["JsonNativeValue"]
    | dict[str, "JsonNativeValue"]
)


class JsonStoreCommand(BaseModel):
    """Common command structure for future service actions."""

    model_config = ConfigDict(extra="forbid")

    entry_id: str = Field(min_length=1)
    document_id: str = Field(min_length=1)


@dataclass(slots=True)
class JsonSqliteStoreRuntimeData:
    """Per-config-entry runtime state reserved for later persistence components."""

    entry_id: str
    loaded_document_count: int = 0


type JsonSqliteStoreConfigEntry = ConfigEntry[JsonSqliteStoreRuntimeData]


def json_value_type_name(value: JsonNativeValue) -> str:
    """Return a stable type name used in bootstrap diagnostics and tests."""
    return type(value).__name__
