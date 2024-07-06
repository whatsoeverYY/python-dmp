import os
import main
from jobs.update_new_module_files import my_crew
from func.camel_case_transform import to_camel_case, to_pascal_case, to_kebab_case
from func.read_file import read_file
from func.create_file import create_file


def replace_path_name(path: str, new_name: str) -> str:
    return path.replace('templateCode', to_camel_case(new_name)).replace('TemplateCode', to_pascal_case(new_name))


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

excluded_files = [
    'domains/templateCodeDomain/enum.ts',
    'types/TemplateCodeType.ts',
]

enum_file = 'domains/templateCodeDomain/enum.ts'
type_file = 'types/TemplateCodeType.ts'

# 手动更新enum
need_update_files = [
    # '/views/templateCode/detail/TemplateCodeEditPage.tsx',
    # '/views/templateCode/BaseTemplateCodeListPage.tsx',
    # '/views/templateCode/TemplateCodeRecycleBin.tsx',
    '/views/templateCode/TemplateCodePreviewList.tsx',
]

# LLM更新配置
need_update_by_llm_files = [
    '/domains/templateCodeDomain/entity.ts',
    '/domains/templateCodeDomain/transform.ts',
    '/views/templateCode/composition/useTemplateCodeDocEdit.tsx',
    '/views/templateCode/composition/useTemplateCodeListColumns.tsx',
    '/views/templateCode/composition/useTemplateCodeSearchFormItems.tsx',
    '/views/templateCode/locales/cn.ts',
]


def read_files_in_directory(directory_path):
    try:
        new_enum_file = '',
        new_type_file = ''
        new_need_update_files = []
        new_need_update_by_llm_files = []
        # 遍历文件夹中的所有文件和子文件夹
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)  # 模板文件路径
                file_content = read_file(file_path)  # 模板文件内容
                new_file_path = replace_path_name(os.path.join(replace_root_path(root), file), new_module_name)  # 新文件路径
                new_module = new_module_name + "(" + new_module_name_cn + ")"  # 新模块名称
                new_file_content = replace_all_template_code(file_content, new_module_name, new_module_name_cn)  # 新文件内容
                is_excluded = any(file in file_path for file in excluded_files)
                is_need_update = any(file in file_path for file in need_update_files)
                is_need_update_by_llm = any(file in file_path for file in need_update_by_llm_files)
                if file in enum_file:
                    new_enum_file = new_file_path
                if file in type_file:
                    new_type_file = new_file_path
                if is_need_update:
                    new_need_update_files.append(new_file_path)
                if is_need_update_by_llm:
                    new_need_update_by_llm_files.append(new_file_path)
                if not is_excluded:
                    create_file(new_file_path, new_file_content)  # 创建excluded_files之外的所有基础文件

        for file in new_need_update_files:
            inputs = {
                "file": main.BASE_ROUTE + file,
                "enum": new_enum_file
            }
            my_crew.kickoff(inputs=inputs)
            print('my_crew.usage_metrics', my_crew.usage_metrics)
        for file in new_need_update_by_llm_files:
            inputs = {
                "file": main.BASE_ROUTE + file,
                "enum": new_enum_file
            }
            print('inputs2', inputs)
            # my_crew.kickoff(inputs=inputs)
            # print('my_crew.usage_metrics', my_crew.usage_metrics)
    except Exception as e:
        print(f"发生错误: {e}")


# 调用函数，传入要读取的文件夹路径
directory_template_path = main.BASE_ROUTE + '_template_code'
read_files_in_directory(directory_template_path)
