from fastapi import FastAPI, APIRouter

SERVER_ID = "104"

app = FastAPI(root_path=f"/usr/{SERVER_ID}")

router = APIRouter()


@router.get("/")
def read_root():
    return {"message": "hello", "status": "online"}


@router.get("/about")
def read_about():
    return {
        "module": "Dynamic Web Applications",
        "framework": "FastAPI",
        "architecture": "Decoupled API-First",
    }


@router.get("/greet")
def greet_user(name: str = "World", repeat: int = 1):
    return {"greeting": f"Hello, {name}!", "messages": [f"Welcome, {name}!"] * repeat}


app.include_router(router)
