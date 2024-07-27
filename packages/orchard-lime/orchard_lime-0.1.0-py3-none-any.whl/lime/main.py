from fastapi import FastAPI, HTTPException, Request
import httpx
import random
import logging

from lime.load_config import load_config
from lime.config import Config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load config from local file
lime_config: Config = load_config("lime.yaml")
OPENAI_API_KEY = lime_config.maas.api_key
OPENAI_BASE_URL = lime_config.maas.base_url
AVIALABLE_MODELS = lime_config.maas.models
DEFAULT_MODEL = lime_config.maas.default_model

app = FastAPI()

def update_model(body):
    origin_model = body["model"]
    if origin_model in AVIALABLE_MODELS:
        logger.info(f"Request model {origin_model} is available")
    else:
        if DEFAULT_MODEL == "":
            random_model = random.choice(AVIALABLE_MODELS)
            body["model"] = random_model
            logger.info(f"Request model {origin_model} is not available, change to random model {random_model}")
        else:
            body["model"] = DEFAULT_MODEL
            logger.info(f"Request model {origin_model} is not available, change to default model {DEFAULT_MODEL}")


async def forward_request(request: Request, endpoint: str):
    async with httpx.AsyncClient() as client:
        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        }
        body = await request.json()

        # Update the "model" parameter with the custom model string
        #if "model" in body:
        #    body["model"] = "THUDM/glm-4-9b-chat"
        update_model(body)

        response = await client.post(f"{OPENAI_BASE_URL}/{endpoint}", json=body, headers=headers)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        return response.json()

@app.post("/v1/chat/completions")
async def chat_completions(request: Request):
    return await forward_request(request, "chat/completions")

@app.post("/v1/completions")
async def completions(request: Request):
    return await forward_request(request, "completions")

@app.post("/v1/edits")
async def edits(request: Request):
    return await forward_request(request, "edits")

@app.post("/v1/embeddings")
async def embeddings(request: Request):
    return await forward_request(request, "embeddings")

@app.post("/v1/audio/transcriptions")
async def audio_transcriptions(request: Request):
    return await forward_request(request, "audio/transcriptions")

@app.post("/v1/audio/translations")
async def audio_translations(request: Request):
    return await forward_request(request, "audio/translations")

@app.get("/v1/models")
async def models():
    async with httpx.AsyncClient() as client:
        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}"
        }
        response = await client.get(f"{OPENAI_BASE_URL}/models", headers=headers)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        return response.json()

@app.get("/v1/models/{model}")
async def model(model: str):
    async with httpx.AsyncClient() as client:
        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}"
        }
        response = await client.get(f"{OPENAI_BASE_URL}/models/{model}", headers=headers)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        return response.json()
