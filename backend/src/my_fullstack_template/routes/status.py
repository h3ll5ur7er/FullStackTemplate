from fastapi import APIRouter
from typing import Literal

router = APIRouter()

from pydantic import BaseModel

class StatusResponse(BaseModel):
    status: Literal["ok", "error"]

@router.get("/status", response_model=StatusResponse)
def get_status():
    return {"status": "ok"}
