""""""

import sys
import asyncio

async def main() -> None:
    """"""

    try:
        raise Exception(123)
    except Exception as err:
        await logger.info(123)

if __name__ == "__main__":
    logger: Logger = Logger.with_default_handlers(
        name=__name__
    )
    
    asyncio.run(main())
