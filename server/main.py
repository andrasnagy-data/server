"""
Main entry point for application.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import server.api.user as user

app = FastAPI()

app.include_router(user.router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
