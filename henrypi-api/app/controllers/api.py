import logging

from fastapi import APIRouter

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/hello")
def get_scan_by_id(name: str):
    return {
        'hello': name,
    }
