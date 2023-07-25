# LLM Workflow Engine (LWE) Hugging Face Hub Provider plugin

Hugging Face Hub Provider plugin for [LLM Workflow Engine](https://github.com/llm-workflow-engine/llm-workflow-engine)

Access to [Hugging Face Hub](https://huggingface.co/models) models.

## Installation

### Export API key

Grab an Hugging Face Hub API key from [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

Export the key into your local environment:

```bash
export HUGGINGFACEHUB_API_TOKEN=<API_KEY>
```

### From packages

Install the latest version of this software directly from github with pip:

```bash
pip install git+https://github.com/llm-workflow-engine/lwe-plugin-provider-huggingface-hub
```

### From source (recommended for development)

Install the latest version of this software directly from git:

```bash
git clone https://github.com/llm-workflow-engine/lwe-plugin-provider-huggingface-hub.git
```

Install the development package:

```bash
cd lwe-plugin-provider-huggingface-hub
pip install -e .
```

## Configuration

Add the following to `config.yaml` in your profile:

```yaml
plugins:
  enabled:
    - provider_huggingface_hub
    # Any other plugins you want enabled...
```

## Usage

From a running LWE shell:

```
/provider huggingface_hub
/model repo_id gpt2
```
