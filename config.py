from pathlib import Path
import os

TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise RuntimeError("TOKEN is not set")

BASE_DIR = Path(__file__).resolve().parent
IMAGES_DIR = BASE_DIR / "images"
