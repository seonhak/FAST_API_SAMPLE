from schemas import LogDocument
from core.exceptions import ServiceError
from fastapi import status
async def search_log_documents(query: str):
    if query == "error":
        raise ServiceError("테스트용 서비스 에러 발생!", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    if query == "notfound":
        raise ServiceError("문서를 찾을 수 없습니다.", status_code=status.HTTP_404_NOT_FOUND, data=None)
    # 실제 Azure Search 연동 대신 임시 결과 반환
    return [
        LogDocument(
            document_id="log1",
            creator="userA",
            modifier="userB",
            created_at="2025-09-01T10:00:00",
            modified_at="2025-09-01T12:00:00",
            content=f"검색어({query})가 포함된 로그 내용"
        )
    ]