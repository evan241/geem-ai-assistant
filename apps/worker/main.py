import asyncio

from geem_ai.shared.infrastructure.configuration.settings import get_settings


async def run() -> None:
    get_settings()

    while True:
        await asyncio.sleep(60)


if __name__ == "__main__":
    asyncio.run(run())
