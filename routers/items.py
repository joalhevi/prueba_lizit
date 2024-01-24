from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from services.item_service import ItemsService
from schemas.items_schemas import ItemSchema
items_router = APIRouter()


@items_router.get('/items', tags=['Items'])
def get_items():
    result = ItemsService().get_items()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@items_router.get('/items/{id}', tags=['Items'])
def get_items(id: int):
    result = ItemsService().get_item(id)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@items_router.post("/items", tags=['Items'])
def create_movie(item: ItemSchema):
    new_item = ItemsService().store_item(item)
    return JSONResponse(status_code=200, content=jsonable_encoder(new_item))

