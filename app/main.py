from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from redis import asyncio as aioredis
from app.routers import admin, common


app = FastAPI()
app.include_router(admin.router)
app.include_router(common.router)


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://redis", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="api:cache")


@app.get("/")
@cache(expire=30)  # конечно все это ерунда, но раз надо с кешированием ... 
def main() -> str:
    return "Bienvenido a nuestro servicio!"




