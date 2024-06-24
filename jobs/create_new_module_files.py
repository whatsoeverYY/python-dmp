import os
import main
from agents.create_new_module import my_crew
from func.camel_case_transform import to_camel_case, to_pascal_case


def replace_path_name(path: str, new_name: str) -> str:
    return path.replace('templateCode', to_camel_case(new_name)).replace('TemplateCode', to_pascal_case(new_name))


def replace_root_path(root: str) -> str:
    return root.replace('_template_code', 'src')


new_module_name = main.NEW_MODULE_NAME
new_module_name_cn = main.NEW_MODULE_NAME_CN


def read_files_in_directory(directory_path):
    try:
        # 遍历文件夹中的所有文件和子文件夹
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                print(f"文件路径: {file_path}")
                new_file_path = replace_path_name(os.path.join(replace_root_path(root), file), new_module_name)
                print(f"需要生成的文件路径: {new_file_path}")

                new_module = new_module_name + "(" + new_module_name_cn + ")"
                my_crew.kickoff(inputs={"file": file_path, "file_path": new_file_path, "new_module": new_module})
    except Exception as e:
        print(f"发生错误: {e}")


# 调用函数，传入要读取的文件夹路径
directory_template_path = main.BASE_ROUTE + '_template_code'
read_files_in_directory(directory_template_path)
