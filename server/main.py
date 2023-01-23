"""
Main entry point for application.
"""
from fastapi import FastAPI

import server.api.user as user

app = FastAPI()

app.include_router(user.router)
