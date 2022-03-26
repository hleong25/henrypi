import logging

import uvicorn
from fastapi import FastAPI

from app.controllers import api
from app.controllers.exception_handlers import setup_exception_handlers

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    )

logger = logging.getLogger(__name__)

app = FastAPI()

setup_exception_handlers(app)

app.include_router(api.router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=80, log_level="info")
