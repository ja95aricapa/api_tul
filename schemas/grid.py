from __future__ import annotations

from typing import List

from pydantic import BaseModel


class Model(BaseModel):
    start_point: List[int]
    end_point: List[int]

    class Config:
        schema_extra = {
            "example": {
                "start_point": [0,0],
                "end_point": [1,1],
            }
        }