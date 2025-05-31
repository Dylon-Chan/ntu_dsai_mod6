import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
    TELEGRAM_API_KEY = os.environ.get('TELEGRAM_API_KEY')
    TELEGRAM_DOMAIN_URL = os.environ.get('TELEGRAM_DOMAIN_URL')