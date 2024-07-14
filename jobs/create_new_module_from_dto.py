import main
from create_new_base_module_files import generate_files_in_directory
from update_base import update_base_files
from update_base_by_whole import update_base_files_by_whole
from update_new_module_files import update_new_module_files
from update_new_module_files_v2 import update_new_module_files_by_type_v2, update_new_module_files_by_enum_v2

# I tried reusing the same input, I must stop using this action input. I'll try something else instead.

generate_files_in_directory(main.BASE_ROUTE + '_template_code')
# 检查21个基础文件正常生成(不包含enum和type文件)
print('步骤一：21个基础文件已生成')

update_base_files()
update_base_files_by_whole()
# 检查5个配置文件正常更新
print('步骤二：5个配置文件已更新')

update_new_module_files()
print('步骤三：4个文件已更新')
update_new_module_files_by_type_v2()
print('步骤四：2个文件已更新')
update_new_module_files_by_enum_v2()
print('步骤五：4个文件已更新')
# 检查10个文件是否被正常更新
print('---------- 结束 ---------- ')
