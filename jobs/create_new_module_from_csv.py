import main
from create_new_base_module_files import generate_files_in_directory
from update_base import update_base_files
from update_base_by_whole import update_base_files_by_whole
from create_new_module_enum import create_enum
from agents.create_type import create_type
from create_new_module_type import create_new_type
from update_new_module_type_v2 import update_type_v2
from update_new_module_files import update_new_module_files
from update_new_module_files_v2 import update_new_module_files_by_type_v2, update_new_module_files_by_enum_v2

generate_files_in_directory(main.BASE_ROUTE + '_template_code')
# 检查21个基础文件正常生成(不包含enum和type文件)

# 检查LLM接口返回的Action Input格式是否正确，不正确则修正格式

update_base_files()
update_base_files_by_whole()
# 检查5个配置文件正常更新

create_enum()
# 检查enum.ts文件是否正确生成

create_type()
create_new_type()
update_type_v2()
# 检查Type.ts文件是否正确生成

update_new_module_files()
update_new_module_files_by_type_v2()
update_new_module_files_by_enum_v2()
# 检查10个文件是否被正常更新
