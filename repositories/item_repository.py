from datetime import datetime

from models.items import Item as ItemModel
from schemas.items_schemas import ItemSchema


class ItemRepository:
    def __init__(self, db) -> None:
        self.db = db

    def get_items(self):
        result = self.db.query(ItemModel).all()
        return result

    def store_item(self, item: ItemSchema):
        new_item = ItemModel(
            name=item.name,
            price=item.price,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        self.db.add(new_item)
        self.db.commit()
        return new_item

    def get_item(self, id):
        result = self.db.query(ItemModel).filter(ItemModel.id == id).one_or_none()
        return result
