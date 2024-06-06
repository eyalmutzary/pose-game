from datetime import datetime
from http import HTTPStatus
from typing import List, Optional
from uuid import uuid4

from config.constants import TEST_SCHEMA_VERSION
from controller.context_manager import build_request_context
from fastapi import APIRouter, Depends
from models.api_schemas.tests_schema import (
    CreateTestBodySchema,
    ExecuteTestBodySchema,
    UpdateTestBodySchema,
)
from models.base import GenericResponseModel
from models.test import DescriptionType, TestModel
from models.test_description import TestGroup
from services.test_service import TestService
from utils.exceptions import AppException
from utils.response_builder import build_api_response

test_router = APIRouter(prefix="/tests", tags=["tests"])


@test_router.post("/execute/{id}", status_code=HTTPStatus.OK, response_model=GenericResponseModel)
async def execute_test(id: str, req_body: ExecuteTestBodySchema, _=Depends(build_request_context)):
    test_model: TestModel = await TestService.execute_test(test_id=id, equipment=req_body.test_equipment)
    response = GenericResponseModel(status_code=HTTPStatus.OK, data=test_model)
    return build_api_response(response)