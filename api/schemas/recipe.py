from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, Field


class Recipe(BaseModel):
    id: int
    name: str = Field(example="至高のポテトサラダ")
    url: str = Field(max_length=300, example="https://bazurecipe.com/レシピ名")
