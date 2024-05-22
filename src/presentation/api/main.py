import logging

import uvicorn
from fastapi import FastAPI

from src.presentation.api.config import ApiConfig
from src.presentation.api.graphql import setup_grapqhl
from src.presentation.api.http import setup_http

logger = logging.getLogger(__name__)


def init_api(debug: bool = __debug__) -> FastAPI:
    logger.debug("Init API")
    app = FastAPI(debug=debug, title="http://pre-recover.com", version="0.0.1")
    setup_http(app)
    setup_grapqhl(app)
    return app


async def start_api(application: FastAPI, api_config: ApiConfig) -> None:
    config = uvicorn.Config(
        app=application,
        host=api_config.host,
        port=api_config.port,
        # log_level=logging.INFO,
        # log_config=None,
    )
    server = uvicorn.Server(config)
    logger.info("Running server")

    await server.serve()
