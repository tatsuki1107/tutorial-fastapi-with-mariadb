from fastapi import FastAPI, APIRouter
from routers.user import router as user_router

router = APIRouter()
router.include_router(
    user_router,
    prefix="/api/users",
    tags=["users"]
)

app = FastAPI()
app.include_router(router)

@app.get('/api/items')
async def read_items():
    return { "item_id": "123" }

