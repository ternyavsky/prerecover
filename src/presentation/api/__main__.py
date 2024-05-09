import asyncio

from .config import Config
from src.presentation.api.main import init_api, start_api
from src.infrastructure.toml_loader import load_config


async def main() -> None:
    config = load_config(Config)
    app = init_api(config.api.debug)
    await start_api(app, config.api)


if __name__ == "__main__":
    asyncio.run(main())
