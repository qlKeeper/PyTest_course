from pydantic import BaseModel, validator, Field


class Post(BaseModel):
    id: int =  Field(le=2)
    title: str
    # name: str = Field(alias="_name")

    # @validator("id")
    # def check_id(cls, v):
    #     if v != 1:
    #         print('id = ', v)
    #         raise ValueError("Id value is not correct")
    #     else:
    #         return v






# {'id': 1, 'title': 'Post 1', '_name': 'Igor'}