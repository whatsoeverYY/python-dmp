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

print(DASHSCOPE_API_KEY)

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
