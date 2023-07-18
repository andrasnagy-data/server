from app import __version__ as version
from app.config import Settings, get_settings
from fastapi import APIRouter, Depends

router = APIRouter(tags=["root"])


@router.get("/")
async def root(settings: Settings = Depends(get_settings)):
    return {
        "version": version,
        "environment": settings.environment,
        "testing": settings.testing,
    }
