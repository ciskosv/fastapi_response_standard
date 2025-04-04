# fastapi_response_standard

Este paquete proporciona un estándar reutilizable para manejar respuestas y errores en aplicaciones FastAPI.

Proporciona:

- Middleware global para capturar errores 500.
- Manejadores de errores para JWT, validación, 404, 403, etc.
- Estructura uniforme de respuesta (`success`, `message`, `data`, `error_code`, `retryable`).
- Códigos de error centralizados (`error_codes.py`).
- Manejadores listos para integración con JWT y rate limiting.

---

## Instalación

Instalación desde GitHub:

```bash
pip install git+https://github.com/ciskosv/fastapi_response_standard.git@main
```

---

## Uso

### 1. Importación y configuración básica

```python
from fastapi import FastAPI
from jose import JWTError
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from fastapi_response_standard import (
    CatchAllMiddleware,
    jwt_error_handler,
    success_response,
    error_response
)

from fastapi_response_standard.common_exception_handlers import (
    not_found_handler,
    validation_error_handler
)

app = FastAPI()

# Middleware global para capturar errores no manejados
app.add_middleware(CatchAllMiddleware)

# Manejadores de errores personalizados
app.add_exception_handler(JWTError, jwt_error_handler)
app.add_exception_handler(StarletteHTTPException, not_found_handler)
app.add_exception_handler(RequestValidationError, validation_error_handler)
```

---

### 2. Ejemplo de rutas

```python
@app.get("/ok")
def ok():
    return success_response({"mensaje": "Todo bien"})

@app.get("/error-controlado")
def error_controlado():
    return error_response(
        message="Esto es un error de negocio",
        error_code="VALIDATION_ERROR",
        retryable=False
    )

@app.get("/error-no-controlado")
def error_no_controlado():
    raise ValueError("Esto lanza error 500")

@app.get("/jwt")
def jwt_error():
    raise JWTError("Token inválido de prueba")
```

---

## Estructura de respuesta esperada

### Éxito:

```json
{
  "success": true,
  "message": "Operación exitosa.",
  "data": {...},
  "error_code": null,
  "retryable": false
}
```

### Error:

```json
{
  "success": false,
  "message": "Token inválido.",
  "data": null,
  "error_code": "INVALID_TOKEN",
  "retryable": false
}
```

---

## Códigos de error

Están centralizados en `error_codes.py`. Algunos ejemplos:

- `INTERNAL_ERROR`
- `VALIDATION_ERROR`
- `TOKEN_EXPIRED`
- `INVALID_TOKEN`
- `NOT_FOUND`
- `FORBIDDEN`
- `TOO_MANY_REQUESTS`

---

## Licencia

MIT © [ciskosv](https://github.com/ciskosv)
