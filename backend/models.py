from pydantic import BaseModel
from sqlmodel import Field, SQLModel
from typing import Annotated
from fastapi import Form

# Model for files
class SingleFile (SQLModel,table = True):
    id : int | None = Field(default = None,primary_key = True)
    content : str = Field(index = True)
    doc_type : str | None = Field(default='text',index = True)
    is_edited : bool = Field(default = False)
    user_id : int = Field(foreign_key = "user.id")

# Model for User
class User (SQLModel,table = True):
      id: int = Field(default = None,primary_key = True)
      username: str
      email: str
      password: str

class Register_User (BaseModel):
        username: Annotated[
        str,
        Form(),
    ]
        email: Annotated[
        str,
        Form(),
    ]
        password: Annotated[
        str,
        Form(),
    ]

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData (BaseModel):
    username: str


class SingleFile_Create (BaseModel):
    content : str = Field(index = True)

class SingleFile_Edit (BaseModel):
    content : str = Field(index = True)
    is_edited : bool = Field(default = True)
    doc_type : str | None = Field(default='text',index = True)