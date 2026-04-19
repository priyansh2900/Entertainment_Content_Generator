import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai

from retriever import retrieve_context
from prompt_engine import build_prompt

load_dotenv()

app = FastAPI(title="Entertainment Content Generator API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gemini-2.5-flash")

print("GOOGLE_API_KEY loaded:", bool(GOOGLE_API_KEY))
print("MODEL_NAME loaded:", MODEL_NAME)

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel(MODEL_NAME)

class GenerateRequest(BaseModel):
    topic: str
    genre: str
    mood: str
    scene_length: str

@app.get("/")
def home():
    return {"message": "Entertainment Content Generator API is running"}

@app.post("/generate")
def generate_content(data: GenerateRequest):
    try:
        search_query = f"{data.topic} {data.genre} {data.mood} screenplay scene"
        context = retrieve_context(search_query)

        prompt = build_prompt(
            topic=data.topic,
            genre=data.genre,
            mood=data.mood,
            scene_length=data.scene_length,
            context=context
        )

        response = model.generate_content(
            f"You are a professional entertainment content generator.\n\n{prompt}"
        )

        output = response.text

        return {
            "topic": data.topic,
            "genre": data.genre,
            "mood": data.mood,
            "scene": output,
            "retrieved_context": context
        }

    except Exception as e:
        return {"error": str(e)}