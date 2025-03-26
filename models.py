from uuid import UUID
from datetime import datetime
from dataclasses import dataclass

from mopyx import model
from db import search


@model
class Item:
    def __init__(self, name='', unit_price=0, qty=1):
        self.name = name
        self.unit_price = unit_price
        self._qty = qty

    @property
    def item_total(self):
        return self.unit_price * self.qty

    @property
    def qty(self):
        return self._qty

    @qty.setter
    def qty(self, qty):
        self._qty = qty

    def __repr__(self):
        return f"{self.name}" # , {self.unit_price}, {self.qty}"

@model
class Order():
    def __init__(self, id: UUID):
        self.id: UUID
        self.number: int = 0
        self.datetime: datetime = 0
        self.date: str = ""
        self.time: str = ""
        self.items: [Item] = []
        self.reset()

    def reset(self):
        self.id = self._get_new_number()
        self.datetime = datetime.now()
        self.date = self.datetime.strftime("%d-%m-%Y")
        self.time = self.datetime.strftime("%H:%M:%S")
        self.items: [Item] = []

    def _get_new_number(self):
        return 1  # todo

    def has_items(self):
        return len(self.items) > 0

    def length(self):
        return len(self.items)


    # Вынесено в handler
    # def change_qty(self, qty, index=None):
    #     assert self.has_items(), "No items in order"
    #     if index is None:
    #         index = len(self.items) - 1
    #     #     index = self.selectedItemIndex
    #     # assert index < len(self.items), f"Индекс выходит за границы массива ({self.selectedItemIndex})"
    #
    #     item = self.items[index]
    #     #print(f"index: {self.selectedItemIndex}, item: {item}")
    #     item.qty = qty


    @property
    def total(self):
        res = 0
        for item in self.items:
            res += item.item_total
        return res

    def __str__(self):
        return f"Order. Date: {self.date}, time: {self.time}, {self.length()} item/s, total: {self.total}"

def main():
    order1 = Order()


if __name__ == '__main__':
    main()