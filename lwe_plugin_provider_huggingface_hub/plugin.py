"""LWE huggingface hub provider integration."""

from __future__ import annotations

from typing import Any
import os

from langchain_huggingface import HuggingFaceEndpoint
from typing_extensions import override

from lwe.core.provider import PresetValue, Provider

HUGGINGFACE_DEFAULT_MODEL = "gpt2"


class CustomHuggingFaceEndpoint(HuggingFaceEndpoint):

    def __init__(self, **kwargs: Any) -> None:
        kwargs["huggingfacehub_api_token"] = os.getenv("HUGGINGFACEHUB_API_TOKEN")
        if "endpoint_url" not in kwargs:
            kwargs["repo_id"] = HUGGINGFACE_DEFAULT_MODEL
        super().__init__(**kwargs)


class ProviderHuggingfaceHub(Provider):
    """
    Access to Hugging Face Hub models
    """

    @property
    @override
    def model_property_name(self) -> str:
        return "repo_id"

    @property
    @override
    def capabilities(self) -> dict[str, bool]:
        return {
            "validate_models": False,
        }

    @property
    @override
    def default_model(self) -> str:
        return HUGGINGFACE_DEFAULT_MODEL

    @property
    @override
    def static_models(self) -> dict[str, dict[str, int]]:
        return {
            "gpt2": {
                "max_tokens": 512,
            },
        }

    @override
    def llm_factory(self) -> type[CustomHuggingFaceEndpoint]:
        return CustomHuggingFaceEndpoint

    @override
    def customization_config(self) -> dict[str, Any]:
        return {
            "repo_id": PresetValue(str, options=self.available_models),
            "model_kwargs": dict,
            "task": PresetValue(str, include_none=True),
        }
