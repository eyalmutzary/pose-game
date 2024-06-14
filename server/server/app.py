from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from pydantic import ValidationError
from utils.exceptions import AppException

from controller import image_controller

from .exception_handler_layer import (
    application_exception_handler,
    general_exception_handler,
    request_validation_exception_handler,
    validation_exception_handler,
)

app = FastAPI()

# * Middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (security risk)
    allow_credentials=True,  # Allow cookies (only works with specific origins)
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# * Routers
app.include_router(image_controller.image_router)

# * Exception Handlers
app.add_exception_handler(RequestValidationError, request_validation_exception_handler)
app.add_exception_handler(ValidationError, validation_exception_handler)
app.add_exception_handler(AppException, application_exception_handler)
app.add_exception_handler(Exception, general_exception_handler)
