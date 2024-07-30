from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv(), override=True)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
