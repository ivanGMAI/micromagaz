from fastapi import Path, APIRouter
from typing import Annotated

router = APIRouter(prefix='/items', tags=['ITems'])

@router.get("/")
def list_items():
    return [
        "Item1",
        "Item2",
        "Item3",
    ]


@router.get("/latest/")
def get_latest_item():
    return {"item": {"id": "0", "name": "latest"}}


@router.get("/{item_id}/")
def get_item_by_id(item_id: Annotated[int,Path(ge=1,lt=10**6)]):
    return {
        "item": {
            "id": item_id,
        },
    }
