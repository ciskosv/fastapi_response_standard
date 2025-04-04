from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import JSONResponse
from .response_utils import error_response
from .error_codes import INTERNAL_ERROR
import traceback
import uuid

class CatchAllMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        try:
            return await call_next(request)
        except Exception as e:
            trace_id = str(uuid.uuid4())
            return JSONResponse(
                status_code=500,
                content=error_response(
                    message="Error inesperado en el servidor.",
                    error_code=INTERNAL_ERROR,
                    retryable=True,
                    data={"error": str(e), "trace_id": trace_id, "trace": traceback.format_exc()}
                )
            )
