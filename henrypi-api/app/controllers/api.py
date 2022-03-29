import logging

from fastapi import APIRouter
from starlette.responses import Response

from app.services.video_control.video_control_service import VideoControlService

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/hello")
def get_scan_by_id(name: str):
    return {
        'hello': name,
    }


@router.post('/video/start')
def video_start():
    VideoControlService.get_instance().auto_start_all()
    return Response(status_code=204)


@router.post('/video/stop')
def video_stop():
    VideoControlService.get_instance().shutdown_all()
    return Response(status_code=204)
