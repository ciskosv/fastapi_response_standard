def success_response(data=None, message="Operación exitosa."):
    return {
        "success": True,
        "message": message,
        "data": data,
        "error_code": None,
        "retryable": False
    }

def error_response(message, error_code="INTERNAL_ERROR", retryable=True, data=None):
    return {
        "success": False,
        "message": message,
        "data": data,
        "error_code": error_code,
        "retryable": retryable
    }
