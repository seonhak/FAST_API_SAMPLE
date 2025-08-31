from fastapi import APIRouter, status
from services import search_log_documents
from schemas import LogDocument, LogQuery, CommonResponse
from typing import List

router = APIRouter()

@router.post("/", response_model=CommonResponse[List[LogDocument]])
async def read_logs(payload: LogQuery):
    try:
        logs = await search_log_documents(payload.query)
        return CommonResponse(
            status_code=status.HTTP_200_OK,
            status_message="OK",
            data=logs
        )
    except Exception as e:
        return CommonResponse(
            status_code=e.status_code,
            status_message=e.message,
            data=None
        )