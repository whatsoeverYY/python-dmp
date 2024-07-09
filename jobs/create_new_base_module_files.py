import os
import main
from func.camel_case_transform import to_camel_case, to_pascal_case, to_kebab_case
from func.read_file import read_file
from func.create_file import create_file
from create_new_module_from_csv import enum_file, type_file, replace_path_name


def replace_root_path(root: str) -> str:
    return root.replace('_template_code', 'src')


def replace_all_template_code(content: str, moduleName: str, moduleNameCn: str) -> str:
    return (content.replace('templateCode', to_camel_case(moduleName)).
            replace('TEMPLATE_CODE', moduleName).
            replace('TemplateCode', to_pascal_case(moduleName)).
            replace('template_code', moduleName.lower()).
            replace('template-code', to_kebab_case(moduleName)).
            replace('模板代码', moduleNameCn))


new_module_name = main.NEW_MODULE_NAME
new_module_name_cn = main.NEW_MODULE_NAME_CN

excluded_files = [enum_file, type_file]


def generate_files_in_directory(directory_path):
    try:
        # 遍历文件夹中的所有文件和子文件夹
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)  # 模板文件路径
                file_content = read_file(file_path)  # 模板文件内容
                new_file_path = replace_path_name(os.path.join(replace_root_path(root), file), new_module_name)  # 新文件路径
                new_module = new_module_name + "(" + new_module_name_cn + ")"  # 新模块名称
                new_file_content = replace_all_template_code(file_content, new_module_name, new_module_name_cn)  # 新文件内容
                is_excluded = any(file in file_path for file in excluded_files)
                if not is_excluded:
                    create_file(new_file_path, new_file_content)  # 创建excluded_files之外的所有基础文件
    except Exception as e:
        print(f"发生错误: {e}")
