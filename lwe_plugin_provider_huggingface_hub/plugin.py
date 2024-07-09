import os

from langchain_huggingface import HuggingFaceEndpoint

from lwe.core.provider import Provider, PresetValue

HUGGINGFACE_DEFAULT_MODEL = 'gpt2'


class CustomHuggingFaceEndpoint(HuggingFaceEndpoint):

    def __init__(self, **kwargs):
        kwargs['huggingfacehub_api_token'] = os.getenv('HUGGINGFACEHUB_API_TOKEN')
        if 'endpoint_url' not in kwargs:
            kwargs['repo_id'] = HUGGINGFACE_DEFAULT_MODEL
        super().__init__(**kwargs)


class ProviderHuggingfaceHub(Provider):
    """
    Access to Hugging Face Hub models
    """

    @property
    def model_property_name(self):
        return 'repo_id'

    @property
    def capabilities(self):
        return {
            'validate_models': False,
        }

    @property
    def default_model(self):
        return HUGGINGFACE_DEFAULT_MODEL

    @property
    def static_models(self):
        return {
            'gpt2': {
                'max_tokens': 512,
            },
        }

    def llm_factory(self):
        return CustomHuggingFaceEndpoint

    def customization_config(self):
        return {
            'repo_id': PresetValue(str, options=self.available_models),
            'model_kwargs': dict,
            'task': PresetValue(str, include_none=True),
        }
