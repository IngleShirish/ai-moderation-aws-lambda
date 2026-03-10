from pydantic import BaseModel
from typing import Optional


class CommentRequest(BaseModel):
    article_id: str
    headline: str
    summary: Optional[str] = None
    comment_id: Optional[str] = None
    comment: str