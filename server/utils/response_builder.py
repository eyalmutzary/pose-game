import http
import uuid
from typing import Dict, List, Union

from controller.context_manager import context_api_id, context_log_meta
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from logger import logger
from models.base import GenericResponseModel


def build_api_response(generic_response: GenericResponseModel) -> JSONResponse:
    try:
        if not generic_response.api_id:
            generic_response.api_id = context_api_id.get() if context_api_id.get() else str(uuid.uuid4())
        if not generic_response.status_code:
            generic_response.status_code = (
                http.HTTPStatus.OK if not generic_response.error else http.HTTPStatus.UNPROCESSABLE_ENTITY
            )
        res = JSONResponse(status_code=generic_response.status_code, content=_build_response_json(generic_response))
        logger.info(
            extra=context_log_meta.get(),
            msg="build_api_response: Generated Response with status_code:" + f"{generic_response.status_code}",
        )
        return res
    except Exception as e:
        logger.error(extra=context_log_meta.get(), msg=f"exception in build_api_response error : {e}")
        return JSONResponse(status_code=generic_response.status_code, content=generic_response.error)


def _build_response_json(generic_response: GenericResponseModel) -> Dict:
    return {
        "api_id": generic_response.api_id,
        "error": generic_response.error,
        "message": generic_response.message,
        "data": jsonable_encoder(generic_response.data),
        "status_code": generic_response.status_code,
    }
