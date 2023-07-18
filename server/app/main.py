import logging
from contextlib import asynccontextmanager

from app.api import root, user
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

log = logging.getLogger("uvicorn")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Start up and tear down logic.
    """
    # get resources
    yield
    # Clean up and release the resources


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(root.router)
    application.include_router(user.router)
    origins = ["*"]
    application.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return application


app = create_application()
