# ruff: noqa: CPY001, N999
"""Realtime Pipecat service for Boson."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .llm import BosonRealtimeLLMService as BosonRealtimeLLMService


__all__ = ["BosonRealtimeLLMService"]


def __getattr__(name: str):
    if name != "BosonRealtimeLLMService":
        raise AttributeError(name)

    from .llm import BosonRealtimeLLMService

    return BosonRealtimeLLMService
