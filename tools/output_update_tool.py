from typing import Optional, Type, Any
from pydantic.v1 import BaseModel, Field
from crewai_tools import BaseTool


class OutputReadToolSchema(BaseModel):
    """Input for OutputUpdateTool."""
    file_path: str = Field(
        ...,
        description="需要修改的文件路径"
    )
    object_str: str = Field(
        ...,
        description="需要修改的对象"
    )
    content: str = Field(
        ...,
        description="修改的代码内容"
    )


left_brace = '{'
right_brace = '}'
left_bracket = '['
right_bracket = ']'
tab_index = '  '


def judge_end_char(start_char: str, end_char: str) -> bool:
    if start_char == left_brace:
        return end_char == right_brace
    if start_char == left_bracket:
        return end_char == right_bracket
    return False


def get_first_non_whitespace_char(s):
    """获取第一个不为空的字符"""
    return next((char for char in s if not char.isspace()), None)


def get_leading_spaces(s):
    leading_spaces = ""
    for char in s:
        if char.isspace():
            leading_spaces += char
        else:
            break
    return leading_spaces


def update_file(file_path: str, object_str: str, content: str):
    start_line_number = -1
    start_line_end_char = ''
    end_line_number = -1
    leading_spaces = ''
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for index, line in enumerate(lines):
            start_char = get_first_non_whitespace_char(line)
            if_obj_line = start_line_number == -1 and object_str in line
            match_braces = judge_end_char(start_line_end_char, start_char) and get_leading_spaces(line) == leading_spaces
            if_obj_end_line = end_line_number == -1 and start_line_number != -1 and index > start_line_number and match_braces

            if if_obj_end_line:
                end_line_number = index
            if if_obj_line:
                start_line_number = index
                start_line_end_char = line.rstrip()[-1]
                leading_spaces += get_leading_spaces(line)
            if start_line_end_char != '' and start_line_end_char != left_brace and start_line_end_char != left_bracket:
                start_line_end_char = line.rstrip()[-1]

        lines.insert(end_line_number, tab_index + leading_spaces + content.lstrip('\n').lstrip() + '\n')
        print(start_line_number, end_line_number, lines)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)


class OutputUpdateTool(BaseTool):
    name: str = "Update a file's content"
    description: str = "A tool that can be used to update a file's content."
    args_schema: Type[BaseModel] = OutputReadToolSchema
    file_path: Optional[str] = None
    object_str: Optional[str] = None
    content: Optional[str] = None

    def __init__(
            self,
            file_path: Optional[str] = None,
            object_str: Optional[str] = None,
            content: Optional[str] = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        if content is not None:
            self.file_path = file_path
            self.object_str = object_str
            self.content = content
            self.description = f"A tool that can be used to print {content}'s content."
            self.args_schema = OutputReadToolSchema
            self._generate_description()

    def _run(
            self,
            **kwargs: Any,
    ) -> Any:
        try:
            file_path = kwargs.get('file_path', self.file_path)
            object_str = kwargs.get('object_str', self.object_str)
            content = kwargs.get('content', self.content)
            print('-------------------- OutputUpdateTool - here is the output content --------------------')
            print(file_path)
            print('-------------------- here is the output content --------------------')
            print(object_str)
            print('-------------------- here is the output content --------------------')
            print(content)
            print('-------------------- OutputUpdateTool - here is the output content --------------------')
            update_file(file_path, object_str, content)
        except Exception as e:
            return f"Fail to update the file {file_path}. Error: {e}"
