from pydantic import BaseModel
from datetime import datetime

class LogQuery(BaseModel):
    query: str

class LogDocument(BaseModel):
    document_id: str
    creator: str
    modifier: str
    created_at: datetime
    modified_at: datetime
    content: str