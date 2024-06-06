import uuid
from contextvars import ContextVar

from fastapi import Depends, Request
from logger import logger
from utils.exceptions import AppException

# context_api_id stores unique id for every request
context_api_id: ContextVar[str] = ContextVar("api_id", default=None)
# context_log_meta stores log meta data for every request
context_log_meta: ContextVar[dict] = ContextVar("log_meta", default={})


async def build_request_context(request: Request):
    context_api_id.set(str(uuid.uuid4()))
    context_log_meta.set(
        {
            "api_id": context_api_id.get(),
            "request_id": request.headers.get("X-Request-ID"),
        }
    )
    logger.info(extra=context_log_meta.get(), msg="REQUEST_INITIATED")