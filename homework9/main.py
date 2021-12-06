import sys
from time import time
import aiohttp
import asyncio
import re


async def fetch_url(url, session):
    regex = re.compile('//[a-z.]+/')
    host = regex.findall(url)[0]
    async with session.get(url, ssl=False) as resp:
        data = await resp.read()
        with open(f'data/url_{host.strip("/")}_{time()}.html', 'wb') as f:
            f.write(data)


def read_url_from_file(file_name):
    with open(file_name, "r") as file:
        return [line.strip() for line in file]


async def main():
    urls = read_url_from_file(sys.argv[2])
    time1 = time()
    queue = asyncio.Queue(maxsize=int(sys.argv[1]))
    async with aiohttp.ClientSession() as session:
        tasks = [
            asyncio.create_task(fetch_url(url, session))
            for url in urls
        ]
        await asyncio.gather(*tasks)
    print(f'Время выполнения: {time() - time1}')


if __name__ == '__main__':
    if len(sys.argv) == 3:
        asyncio.run(main())
    else:
        print('Неверное количество аргументов')
