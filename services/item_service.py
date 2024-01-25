from repositories.item_repository import ItemRepository
from config.database import Session
from schemas.items_schemas import ItemSchema


class ItemsService:
    def __init__(self) -> None:
        pass

    def get_items(self):
        try:
            db = Session()
            result = ItemRepository(db).get_items()
            return result
        except Exception as e:
            return str(e)

    def store_item(self, item: ItemSchema):
        try:
            db = Session()
            result = ItemRepository(db).store_item(item)
            return result
        except Exception as e:
            return str(e)

    def get_item(self, item_id: int):
        try:
            db = Session()
            result = ItemRepository(db).get_item(item_id)
            return result
        except Exception as e:
            return str(e)

    def update_item(self, item_id: int, item: ItemSchema):
        try:
            db = Session()
            result = ItemRepository(db).update_item(item_id, item)
            return result
        except Exception as e:
            return str(e)

    def delete_item(self, item_id: int):
        try:
            db = Session()
            result = ItemRepository(db).delete_item(item_id)
            return result
        except Exception as e:
            return str(e)
