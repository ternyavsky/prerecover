import logging

import uvicorn
from fastapi import FastAPI

logger = logging.getLogger(__name__)


def init_api(debug: bool = __debug__) -> FastAPI:
    logger.debug("Init API")
    app = FastAPI(debug=debug, title="pre-recover.com", version="0.0.1")
    return app


async def start_api(application: FastAPI, api_config=None) -> None:
    config = uvicorn.Config(
        app=application,
        host="0.0.0.0",
        port=8000,
        reload=True,
        # log_level=logging.INFO,
        # log_config=None,
    )
    server = uvicorn.Server(config)
    logger.info("Running server")
    await server.serve()
