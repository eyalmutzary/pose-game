import http
import json

from controller.context_manager import context_log_meta
from fastapi import Request
from fastapi.exceptions import RequestValidationError
from logger import logger
from models.base import GenericResponseModel
from pydantic import ValidationError
from utils.exceptions import AppException
from utils.response_builder import build_api_response


# * Handle validation exceptions of the request body and params
async def request_validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.error(extra=context_log_meta.get(), msg=f"request validation failed {exc.errors()}")
    return build_api_response(
        GenericResponseModel(status_code=http.HTTPStatus.BAD_REQUEST, error="Request Validation Failed", data=exc)
    )


# * Handle validation exceptions on creating pydantic models
async def validation_exception_handler(request: Request, exc: ValidationError):
    logger.error(extra=context_log_meta.get(), msg=f"data validation failed {exc.errors()}")
    return build_api_response(
        GenericResponseModel(
            status_code=http.HTTPStatus.BAD_REQUEST, error="Data Validation Failed", data=exc.errors()
        )
    )


# * Handles application exceptions
async def application_exception_handler(request, exc: AppException):
    logger.error(extra=context_log_meta.get(), msg=f"application exception occurred error: {json.loads(str(exc))}")
    return build_api_response(GenericResponseModel(status_code=exc.status_code, error=exc.message))


# * Handles any other unexpected exceptions
async def general_exception_handler(request, exc: Exception):
    defined_exception: AppException = AppException(status_code=500, message=exc.__str__())
    logger.error(msg=f"general exception occurred error: {json.loads(str(defined_exception))}")
    return build_api_response(
        GenericResponseModel(status_code=defined_exception.status_code, error=defined_exception.message)
    )
