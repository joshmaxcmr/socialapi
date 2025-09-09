from httpx import AsyncClient

async def create_post(body: str, async_client: AsyncClient) -> dict:
    response = await async_client.post("/post", json={"body": body})
    return response.json()