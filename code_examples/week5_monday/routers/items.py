from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix = "/items",
    tags = ["items"],
    responses = {404: {"description": "Item not found"}}
    )

_ITEMS = {
    1: {"item_id": 1, "name": "Keyboard", "price": 49.99, "active": True},
    2: {"item_id": 2, "name": "Mouse", "price": 19.99, "active": False},
}

# GET /items  -> list, with query params for paging + filtering
@router.get("")
def list_items(limit: int = 20, offset: int = 0, active: bool | None = None):
    rows = list(_ITEMS.values())
    if active is not None:
        rows = [r for r in rows if r["active"] == active]
    return rows[offset : offset + limit]


# GET /items/{item_id}  -> one resource, selected by path param
@router.get("/{item_id}")
def get_item(item_id: int):
    item = _ITEMS.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
    return item