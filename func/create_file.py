import os


def create_file(file_path, content):
    try:
        # 确保目标目录存在，如果不存在则创建
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # 打开文件并写入内容
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
    except Exception as e:
        print(f"发生错误: {e}")


