import base64
from http import HTTPStatus
from io import BytesIO

import cv2
import numpy as np
from controller.context_manager import build_request_context
from fastapi import APIRouter, Depends
from models.api_schemas.images_schema import ImageSchema
from models.base import GenericResponseModel
from PIL import Image
from utils.response_builder import build_api_response
from logger import logger
from services.features_analyzer import FeaturesAnalyzer
from services.pose_classifier import PoseClassifier

image_router = APIRouter(prefix="/images", tags=["images"])


@image_router.post("/", status_code=HTTPStatus.OK, response_model=GenericResponseModel)
async def execute_test(image_data: ImageSchema, _=Depends(build_request_context)):
    response = GenericResponseModel(status_code=HTTPStatus.OK, data={})
    return build_api_response(response)


@image_router.post("/analyze", status_code=HTTPStatus.OK, response_model=GenericResponseModel)
async def receive_image(image_base64: ImageSchema, _=Depends(build_request_context)):
    image_data = base64.b64decode(image_base64.image.split(",")[1])
    image = Image.open(BytesIO(image_data))
    decoded_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    features = FeaturesAnalyzer().get_features(decoded_image)
    pose_classifier = PoseClassifier().classify_pose(features)
    response = GenericResponseModel(status_code=HTTPStatus.OK, data=pose_classifier)
    return build_api_response(response)