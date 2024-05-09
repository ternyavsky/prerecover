import asyncio

from src.infrastructure.toml_loader import load_config
from src.presentation.api.main import init_api, start_api

from .config import Config


async def main() -> None:
    config = load_config(Config)
    app = init_api(config.api.debug)
    await start_api(app, config.api)


if __name__ == "__main__":
    asyncio.run(main())
