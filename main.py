from dotenv import load_dotenv
import os

load_dotenv()

BASE_ROUTE = os.getenv('BASE_ROUTE')
ROOT_PATH = os.getenv('ROOT_PATH')
DASHSCOPE_API_KEY = os.getenv('DASHSCOPE_API_KEY')
CHAT_URL = os.getenv('CHAT_URL')
CHAT_AUTHORIZATION = os.getenv('CHAT_AUTHORIZATION')
CHAT_MODEL = os.getenv('CHAT_MODEL')
CHAT_MAX_TOKEN = int(os.getenv('CHAT_MAX_TOKEN'))
CHAT_ENGINE = os.getenv('CHAT_ENGINE')

NEW_MODULE_NAME = os.getenv('NEW_MODULE_NAME')
NEW_MODULE_NAME_CN = os.getenv('NEW_MODULE_NAME_CN')
