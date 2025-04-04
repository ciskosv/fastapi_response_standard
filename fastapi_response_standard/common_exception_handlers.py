# common_exception_handlers.py
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from .response_utils import error_response
from .error_codes import (
    VALIDATION_ERROR,
    NOT_FOUND,
    FORBIDDEN
)

async def not_found_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=404,
        content=error_response(
            message="Ruta no encontrada.",
            error_code=NOT_FOUND,
            retryable=False
        )
    )

async def forbidden_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=403,
        content=error_response(
            message="Acceso no autorizado.",
            error_code=FORBIDDEN,
            retryable=False
        )
    )

async def validation_error_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content=error_response(
            message="Error de validación de datos.",
            error_code=VALIDATION_ERROR,
            retryable=False,
            data=exc.errors()
        )
    )
