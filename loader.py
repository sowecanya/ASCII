from dotenv import load_dotenv
from pathlib import Path
import os


load_dotenv()
env_path = Path('..') / '.env'
load_dotenv(dotenv_path=env_path)


WIDTH_OF_REGION = os.getenv("WIDTH")
HEIGHT_OF_REGION = int(WIDTH_OF_REGION * 2)
TOKEN = os.getenv("BOT_TOKEN")
