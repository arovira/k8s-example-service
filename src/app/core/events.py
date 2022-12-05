from fastapi import FastAPI
from loguru import logger
from prometheus_fastapi_instrumentator import Instrumentator
from typing import Callable

from app.core.config import get_app_settings


def create_start_app_handler(
    app: FastAPI,
    settings: get_app_settings(),
) -> Callable:  # type: ignore
    async def start_app() -> None:
        Instrumentator().instrument(app).expose(app)

    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:  # type: ignore
    @logger.catch
    async def stop_app() -> None:
        print("TODO: Add shutdown procedure")

    return stop_app
