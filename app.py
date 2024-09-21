import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    url = 'http://example.com'
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        print(html)

# Run the main function
if __name__ == '__main__':
    asyncio.run(main())