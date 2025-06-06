from fastapi import FastAPI, Header
from typing import Optional
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Get API key from environment
API_KEY = os.getenv("API_KEY")

app = FastAPI()

@app.get("/")
def index(x_api_key: Optional[str] = Header(None)):
    if x_api_key == API_KEY:
        return {"message": "Hello world"}
    else:
        return {"message": "Access denied. Invalid or missing API key."}
