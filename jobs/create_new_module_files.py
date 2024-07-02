import os
import main
from agents.create_new_module import my_crew
from agents.create_new_module_cn import my_crew_cn
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
    # 'domains/templateCodeDomain/enum.ts',
    # 'types/TemplateCodeType.ts',
]

# 手动更新enum
need_update_files = [
    '/views/templateCode/detail/TemplateCodeEditPage.tsx',
    '/views/templateCode/BaseTemplateCodeListPage.tsx',
    '/views/templateCode/TemplateCodeRecycleBin.tsx',
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
        # 遍历文件夹中的所有文件和子文件夹
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                # print(f"文件路径: {file_path}")
                is_excluded = any(file in file_path for file in excluded_files)
                if not is_excluded:
                    new_file_path = replace_path_name(os.path.join(replace_root_path(root), file), new_module_name)
                    print(f"需要生成的文件路径: {new_file_path}")
                    new_module = new_module_name + "(" + new_module_name_cn + ")"
                    file_content = read_file(file_path)
                    new_file_content = replace_all_template_code(file_content, new_module_name, new_module_name_cn)
                    inputs = {
                        "file": file_content,
                        "file_path": new_file_path,
                        "new_module": new_module
                    }
                    create_file(new_file_path, new_file_content)
                    # my_crew.kickoff(inputs=inputs)
                    # print('new_file_path', new_file_path)
                    # if new_file_path == '/Users/ever/Documents/AI/projects/data-management-platform-frontend/src/domains/translationalMedicineDomain/entity.ts':
                    #     my_crew.kickoff(inputs=inputs)
                    # print('my_crew.usage_metrics', my_crew.usage_metrics)
    except Exception as e:
        print(f"发生错误: {e}")


# 调用函数，传入要读取的文件夹路径
directory_template_path = main.BASE_ROUTE + '_template_code'
read_files_in_directory(directory_template_path)
