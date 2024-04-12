import asyncio

from src.presentation.api.main import init_api, start_api


async def main() -> None:
    app = init_api(True)
    await start_api(app)


if __name__ == "__main__":
    asyncio.run(main())
