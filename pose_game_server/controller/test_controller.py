from datetime import datetime
from http import HTTPStatus
from typing import List, Optional
from uuid import uuid4

from controller.context_manager import build_request_context
from fastapi import APIRouter, Depends
from models.api_schemas.tests_schema import (
    ExampleSchema,
)
from models.base import GenericResponseModel
from utils.exceptions import AppException
from utils.response_builder import build_api_response

test_router = APIRouter(prefix="/tests", tags=["tests"])


@test_router.post("/execute/{id}", status_code=HTTPStatus.OK, response_model=GenericResponseModel)
async def execute_test(id: str, req_body: ExampleSchema, _=Depends(build_request_context)):
    response = GenericResponseModel(status_code=HTTPStatus.OK, data={})
    return build_api_response(response)