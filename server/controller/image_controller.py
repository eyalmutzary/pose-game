import base64
from http import HTTPStatus
from io import BytesIO

import cv2
import numpy as np
from controller.context_manager import build_request_context
from fastapi import APIRouter, Depends
from models.api_schemas.images_schema import AnalyzePose, EstimatePoseProb
from models.base import GenericResponseModel
from PIL import Image
from utils.response_builder import build_api_response
from services.features_analyzer import FeaturesAnalyzer
from services.pose_classifier import PoseClassifier
from logger import logger

image_router = APIRouter(prefix="/images", tags=["images"])


@image_router.get("/", status_code=HTTPStatus.OK, response_model=GenericResponseModel)
async def execute_test(image_data: AnalyzePose, _=Depends(build_request_context)):
    response = GenericResponseModel(status_code=HTTPStatus.OK, data={})
    return build_api_response(response)


@image_router.post("/analyze-pose", status_code=HTTPStatus.OK, response_model=GenericResponseModel)
async def analyze_pose(image_base64: AnalyzePose, _=Depends(build_request_context)):
    image_data = base64.b64decode(image_base64.image.split(",")[1])
    image = Image.open(BytesIO(image_data))
    decoded_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    features = FeaturesAnalyzer().get_features(decoded_image)
    pose_classifier = PoseClassifier().classify_pose(features)
    response = GenericResponseModel(status_code=HTTPStatus.OK, data=pose_classifier)
    return build_api_response(response)

@image_router.post("/estimate-pose-prob", status_code=HTTPStatus.OK, response_model=GenericResponseModel)
async def estimate_pose_prob(image_base64: EstimatePoseProb, _=Depends(build_request_context)):
    image_data = base64.b64decode(image_base64.image.split(",")[1])
    image = Image.open(BytesIO(image_data))
    decoded_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    features = FeaturesAnalyzer().get_features(decoded_image)
    pose_classifier = PoseClassifier().get_pose_probability(features, image_base64.pose_to_check)
    response = GenericResponseModel(status_code=HTTPStatus.OK, data=pose_classifier)
    return build_api_response(response)

@image_router.get("/all-poses", status_code=HTTPStatus.OK, response_model=GenericResponseModel)
async def all_poses(_=Depends(build_request_context)):
    pose_classifier = PoseClassifier().get_all_poses_names()
    response = GenericResponseModel(status_code=HTTPStatus.OK, data=pose_classifier)
    return build_api_response(response)