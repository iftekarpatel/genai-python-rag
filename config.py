import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
MODEL_NAME = os.getenv("MODEL_NAME")
GITHUB_ENDPOINT = os.getenv("GITHUB_ENDPOINT")