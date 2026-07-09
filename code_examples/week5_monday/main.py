from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Pydantic Demo")


from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(
    title="Well-Documented Items API",
    description="Demonstrates docstrings, tags, response models, and errors.",
    version="1.0.0",
)


class ItemOut(BaseModel):
    item_id: int
    name: str
    price: float


class ItemCreate(BaseModel):
    name: str = Field(min_length=1)
    price: float = Field(gt=0)


_DB: dict[int, dict] = {1: {"item_id": 1, "name": "Keyboard", "price": 49.99}}
_next_id = 2


@app.get("/items/{item_id}", response_model=ItemOut, tags=["items"],
         summary="Fetch one item")
def get_item(item_id: int):
    """Return a single item by its **item_id**, or `404` if it does not exist."""
    item = _DB.get(item_id)
    if item is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"Item {item_id} not found")
    return item


@app.post("/items", response_model=ItemOut, status_code=status.HTTP_201_CREATED,
          tags=["items"], summary="Create an item")
def create_item(item: ItemCreate):
    """Create a new item. The server assigns the **item_id**."""
    global _next_id
    record = {"item_id": _next_id, **item.model_dump()}
    _DB[_next_id] = record
    _next_id += 1
    return record