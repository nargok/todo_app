from fastapi import FastAPI, APIRouter

# from todo.controllers.todo import router as todo_router
from todo.routers.todo import router as todo_router

router = APIRouter()
router.include_router(
    todo_router,
    prefix="/todos",
    tags=['todo']
)

app = FastAPI()
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Hello, world"}
