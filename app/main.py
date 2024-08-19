from app.routers import allfoodtruck, food, nearest

from starlette.responses import JSONResponse
from slowapi.errors import RateLimitExceeded
from fastapi import FastAPI, Request

app = FastAPI()

app.include_router(allfoodtruck.router)
app.include_router(food.router)
app.include_router(nearest.router)

@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    response = await call_next(request)
    return response

@app.exception_handler(RateLimitExceeded)
async def rate_limit_exceeded_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"detail": "Rate limit exceeded"},
    )