from pathlib import Path

TOKEN = "8619177224:AAELsPNHGaebNth9LXTjHh3Y5winjvCWarQ"
if not TOKEN:
    raise RuntimeError("TOKEN is not set")

BASE_DIR = Path(__file__).resolve().parent
IMAGES_DIR = BASE_DIR / "images"
