import datetime
from pydantic import BaseModel, Field

# from typing import Optional


class TaskBase(BaseModel):
    title: str | None = Field(None, example="クリーニング")
    # title: Optional[str] = Field(None, example="クリーニング代")
    due_date: datetime.date | None = Field(None, example="2024-12-01")


class TaskCreate(TaskBase):
    pass


class TaskCreateResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True


class Task(TaskBase):
    id: int
    done: bool = Field(False, description="完了フラグ")

    class Config:
        orm_mode = True
