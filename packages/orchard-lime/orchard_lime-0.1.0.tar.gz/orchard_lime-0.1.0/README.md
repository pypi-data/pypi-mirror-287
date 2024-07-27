# Lime

Lime is the MaaS proxy for anonymously access with OpenAI API.

* Compatible with multiple OpenAI API endpoints.
* Allow anonymous access for unregistered users.
* Configurable for free MaaS services and models.

## Install

Install with `pip`.

```
pip install orchard-lime
```

## Setup

Prepare a configuration file named `lime.yaml` with the following content. Change MaaS and API KEY if needed.

```
maas:
  base_url: "https://api.siliconflow.cn/v1"
  api_key: ""
  default_model: ""
  models:
    - "Qwen/Qwen2-7B-Instruct"
    - "Qwen/Qwen2-1.5B-Instruct"
    - "Qwen/Qwen1.5-7B-Chat"
    - "THUDM/glm-4-9b-chat"
    - "THUDM/chatglm3-6b"
    - "01-ai/Yi-1.5-9B-Chat-16K"
    - "01-ai/Yi-1.5-6B-Chat"
    - "google/gemma-2-9b-it"
    - "internlm/internlm2_5-7b-chat"
    - "meta-llama/Meta-Llama-3-8B-Instruct"
    - "meta-llama/Meta-Llama-3.1-8B-Instruct"
    - "mistralai/Mistral-7B-Instruct-v0.2"
```

Start with `uvicorn`.

```
uvicorn lime.main:app --reload --port 10000
```

## Usage

Use HTTP API with curl.

```
curl -X POST "http://127.0.0.1:10000/v1/chat/completions" -H "Content-Type: application/json" -d '{
  "model": "Qwen/Qwen2-7B-Instruct",
  "messages": [{"role": "user", "content": "Who are you?"}]
}'
```

Use [bascket](https://github.com/OrchardUniverse/basket) command.

```
basket maas use Lime

basket model use Qwen/Qwen2-7B-Instruct

basket chat "what is the meaning of life?"
```
