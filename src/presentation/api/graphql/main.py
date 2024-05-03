from fastapi import FastAPI

from .healthcheck import healthcheck_router


def setup_grapqhl(app: FastAPI) -> None:
    app.include_router(healthcheck_router, prefix="/graphql", tags=["graphql"])
