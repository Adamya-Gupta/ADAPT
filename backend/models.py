from sqlmodel import Field, SQLModel

class SingleFile (SQLModel,table = True):
    id : int | None = Field(default = None,primary_key = True)
    content : str = Field(index = True)
    doc_type : str | None = Field(default='text',index = True)
    is_edited : bool = Field(default = False)