# from langchain.tools import BaseTool, StructuredTool, tool
from file_operator.write_file import write_file
from file_operator.read_file import read_file

def create_file(file_path: str, content: str):
    """将content写入file_path文件中"""
    write_file(file_path, 'w', content)

def read_from_file(file_path: str):
    """将content写入file_path文件中"""
    return read_file(file_path)
