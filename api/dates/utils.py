import httpx

async def fetch_fun_fact(month: int, day: int) -> str:
    url = f"http://numbersapi.com/{month}/{day}/date"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.headers.get("content-type")
