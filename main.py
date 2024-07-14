from dotenv import load_dotenv
import os
import re
from func.camel_case_transform import to_kebab_case, to_pascal_case, to_camel_case

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

ENUM_FILE = '/domains/templateCodeDomain/enum.ts'
TYPE_FILE = '/types/TemplateCodeType.ts'


def print_hi(name):
    excluded_files = [
        'domains/templateCodeDomain/enum.ts',
        'types/TemplateCodeType.ts',
    ]
    # 要判断的字符串

    # 使用 any() 函数和列表推导判断
    is_excluded = any(file in name for file in excluded_files)
    print(is_excluded)
    print(to_kebab_case('TRANSLATIONAL_MEDICINE'))
    print(to_pascal_case('TRANSLATIONAL_MEDICINE'))
    print(to_camel_case('TRANSLATIONAL_MEDICINE'))


def searchActionInput(text):
    action_input_pattern = r"[\s]*Action\s*\d*\s*Input\s*\d*\s*:[\s]*(.*)"

    action_input = re.search(action_input_pattern, text).group(1)

    print("Action Input:", action_input)


if __name__ == '__main__':
    a = '/Users/ever/Documents/AI/projects/data-management-platform-frontend/_template_code/domains/templateCodeDomain/enum.ts'
    b = '/Users/ever/Documents/AI/projects/data-management-platform-frontend/_template_code/views/templateCode/locales/cn.ts'
    # print_hi(a)
    # print_hi(b)
    text = '''Action: Update a file's content
Action Input:
```json 
{"file_path": "/Users/ever/Documents/AI/projects/data-management-platform-frontend/src/router/dict/index.ts", "object_str": "DictPermNames", "content": "[DICTYPENAMES.CT_PARAM_TYPE]: { permCode: 'dict.ct_param_type' }"}
```

Observation: The file has been successfully updated.'''
    searchActionInput(text)

