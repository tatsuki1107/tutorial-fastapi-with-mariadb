from fastapi import FastAPI, APIRouter
from routers.user import router as user_router
import uvicorn

router = APIRouter()
router.include_router(
    user_router,
    prefix="/users",
    tags=["users"]
)

app = FastAPI()
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8888)
