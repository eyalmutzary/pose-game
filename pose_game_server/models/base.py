from datetime import datetime
from typing import Any, Optional
from uuid import uuid4

from pydantic.main import BaseModel


class GenericResponseModel(BaseModel):
    """Generic response model for all responses"""

    api_id: Optional[str] = None
    error: Optional[str] = None
    message: Optional[str] = None
    data: Any = None
    status_code: int  # mandatory field


class DBBaseModel(BaseModel):
    """Base model for all models that will be stored in the database"""

    id: str
    created_at: datetime = datetime.now()
    updated_at: Optional[datetime] = datetime.now()
    is_deleted: bool = False
