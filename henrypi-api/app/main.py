import logging

import uvicorn
from fastapi import FastAPI

from app.controllers import api
from app.controllers.exception_handlers import setup_exception_handlers
from scripts.video_ctl import start_video_devices

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    )

logger = logging.getLogger(__name__)

app = FastAPI()

setup_exception_handlers(app)

app.include_router(api.router)

start_video_devices()

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, log_level="info")
