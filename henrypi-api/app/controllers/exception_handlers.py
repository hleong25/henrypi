from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse


def setup_exception_handlers(app: FastAPI):
    app.add_exception_handler(Exception, _default_exception_handler)


def _default_exception_handler(request: Request, ex: Exception):
    return JSONResponse(
        status_code=500,
        content={
            'exception': str(ex),
        }
    )


