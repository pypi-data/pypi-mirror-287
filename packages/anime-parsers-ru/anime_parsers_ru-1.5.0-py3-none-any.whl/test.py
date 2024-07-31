from anime_parsers_ru.parser_kodik_async import KodikParserAsync

import asyncio
from pprint import pprint

parser = KodikParserAsync()

# 53446 610 12ep

async def main():
    #info = await parser.get_info('53446', 'shikimori')
    # info = await parser.get_link('53446', 'shikimori', 1, '610')
    info = await parser.translations('53446', 'shikimori')
    pprint(info)

asyncio.run(main())