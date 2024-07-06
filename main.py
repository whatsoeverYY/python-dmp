from dotenv import load_dotenv
import os
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


if __name__ == '__main__':
    a = '/Users/ever/Documents/AI/projects/data-management-platform-frontend/_template_code/domains/templateCodeDomain/enum.ts'
    b = '/Users/ever/Documents/AI/projects/data-management-platform-frontend/_template_code/views/templateCode/locales/cn.ts'
    print_hi(a)
    print_hi(b)