import os
from dotenv import load_dotenv

# Ladda miljövariabler från .env-filen
load_dotenv()

"""Handles connections to services we need:
Database
API
LLM
Stable Diffusion
"""


class Settings:
    ASTRADB_SECURE_CONNECT_BUNDLE = os.getenv("ASTRADB_SECURE_CONNECT_BUNDLE")
    IMAGE_API_URL = os.getenv("IMAGE_API_URL")


settings = Settings()
