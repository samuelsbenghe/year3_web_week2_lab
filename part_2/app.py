from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

SERVER_ID = "551"

app = FastAPI(root_path=f"/usr/{SERVER_ID}")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()


class ItemCreate(BaseModel):
    title: str = Field(min_length=2, max_length=50)
    price: float = Field(gt=0)


items_db = [
    {"id": 1, "title": "Mechanical Keyboard", "price": 89.99},
    {"id": 2, "title": "USB-C Hub", "price": 24.50},
    {"id": 3, "title": "Wireless Mouse", "price": 45.00},
]


@router.get("/")
def read_root():
    return {"status": "online", "items_count": len(items_db)}


@router.get("/items")
def get_all_items():
    return items_db


@router.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items_db:
        if item["id"] == item_id:
            return item

    raise HTTPException(status_code=404, detail="Item not found")


@router.post("/items", status_code=201)
def create_item(item: ItemCreate):
    new_id = max((i["id"] for i in items_db), default=0) + 1

    new_record = {"id": new_id, "title": item.title, "price": item.price}

    items_db.append(new_record)

    return new_record


@router.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(items_db):
        if item["id"] == item_id:
            removed = items_db.pop(index)

            return {"deleted": removed}

    raise HTTPException(status_code=404, detail=f"Item {item_id} not found")


app.include_router(router)
