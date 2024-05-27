import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class Config:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
