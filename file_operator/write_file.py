def write_file(file_path: str, mode: str, content: str):
    with open(file_path, mode) as variable_name:
        variable_name.write(content)