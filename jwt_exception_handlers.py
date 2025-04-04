from fastapi import Request
from fastapi.responses import JSONResponse
from jose import JWTError, ExpiredSignatureError
from .response_utils import error_response
from .error_codes import INVALID_TOKEN, TOKEN_EXPIRED

async def jwt_error_handler(request: Request, exc: JWTError):
    if isinstance(exc, ExpiredSignatureError):
        return JSONResponse(
            status_code=401,
            content=error_response(
                message="El token ha expirado.",
                error_code=TOKEN_EXPIRED,
                retryable=False
            )
        )
    return JSONResponse(
        status_code=401,
        content=error_response(
            message="Token inválido.",
            error_code=INVALID_TOKEN,
            retryable=False
        )
    )
