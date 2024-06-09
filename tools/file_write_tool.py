from typing import Optional, Type, Any
from pydantic.v1 import BaseModel, Field
from crewai_tools import BaseTool


class FixedFileWriteToolSchema(BaseModel):
    """Input for FileReadTool."""
    pass


class FileWriteToolSchema(FixedFileWriteToolSchema):
    """Input for FileReadTool."""
    file_path: str = Field(
        ...,
        description="Mandatory file full path to write the file"
    )
    content: str = Field(
        ...,
        description="content to write in the file"
    )


class FileWriteTool(BaseTool):
    name: str = "write content into a file"
    description: str = "A tool that can be used to write content into a file."
    args_schema: Type[BaseModel] = FileWriteToolSchema
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
            self.description = f"A tool that can be used to write {content} into {file_path}."
            self.args_schema = FixedFileWriteToolSchema
            self._generate_description()

    def _run(
        self,
        **kwargs: Any,
    ) -> Any:
        try:
            file_path = kwargs.get('file_path', self.file_path)
            content = kwargs.get('content', self.content)
            with open(file_path, 'w') as file:
                return file.write(content)
        except Exception as e:
            return f"Fail to write the file {file_path}. Error: {e}"
