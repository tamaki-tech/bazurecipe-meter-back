from turtle import title
from typing import List
from fastapi import APIRouter

import api.schemas.recipe as recipe_schema

router = APIRouter()


@router.get("/recipes", response_model=List[recipe_schema.Recipe])
async def list_recipes():
    return [
        recipe_schema.Recipe(
            id=1,
            name="至高のポテトサラダ",
            url="https://bazurecipe.com/2020/07/21/%e8%87%b3%e9%ab%98%e3%81%ae%e3%83%9d%e3%83%86%e3%83%88%e3%82%b5%e3%83%a9%e3%83%80/",
        )
    ]
