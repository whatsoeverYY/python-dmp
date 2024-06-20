from typing import Optional, Type, Any
from pydantic.v1 import BaseModel, Field
from crewai_tools import BaseTool
import os


class FixedFileCreateToolSchema(BaseModel):
    """Input for FileCreateTool."""
    pass


class FileCreateToolSchema(FixedFileCreateToolSchema):
    """Input for FileCreateTool."""
    file_path: str = Field(
        ...,
        description="Mandatory file full path to create the file"
    )
    content: str = Field(
        ...,
        description="Mandatory file content to create the file"
    )


class FileCreateTool(BaseTool):
    name: str = "Read a file's content"
    description: str = "A tool that can be used to create a file with the content."
    args_schema: Type[BaseModel] = FileCreateToolSchema
    file_path: Optional[str] = None
    content: Optional[str] = None

    def __init__(
        self,
        file_path: Optional[str] = None,
        content: Optional[str] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        if file_path is not None:
            self.file_path = file_path
            self.content = content
            self.description = f"A tool that can be used to create {file_path} with {content}."
            self.args_schema = FixedFileCreateToolSchema
            self._generate_description()

    def _run(
        self,
        **kwargs: Any,
    ) -> Any:
        try:
            file_path = kwargs.get('file_path', self.file_path)
            content = kwargs.get('content', self.content)
            print('-------------------- FileCreateTool - here is the file_path and content Start--------------------')
            print(file_path)
            print('-------------------- here is the output content --------------------')
            print(content)
            print('-------------------- FileCreateTool - here is the file_path and content End --------------------')
            # 确保目标目录存在，如果不存在则创建
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            # 打开文件并写入内容
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"文件已创建：{file_path}")
        except Exception as e:
            return f"Fail to create the file. Error: {e}"
