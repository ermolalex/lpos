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
    def __init__(self):
        self.id = 0
        self.datetime: datetime = 0
        self.date: str = ""
        self.time: str = ""
        self.items: [Item] = []

    def reset(self):
        self.id = self._get_new_id()
        self.datetime = datetime.now()
        self.date = self.datetime.strftime("%d-%m-%Y")
        self.time = self.datetime.strftime("%H:%M:%S")
        self.items: [Item] = []

    def _get_new_id(self):
        return 1  # todo

    def has_items(self):
        return len(self.items) > 0

    def length(self):
        return len(self.items)

    def add_line(self, plu):
        prod = search(plu)
        if prod is None:
            print(f"Товар с кодом {plu} не найден!")
            return
        item = Item(
            name=prod['name'],
            unit_price=prod['unit_price'],
        )
        self.items.append(item)

        self.selectedItemIndex = len(self.items) - 1
        return self.selectedItemIndex

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

    def storno(self, index=None):
        if self.has_items():
            self.items.pop()



    @property
    def total(self):
        res = 0
        for item in self.items:
            res += item.item_total
        return res




def main():
    order1 = Order()


if __name__ == '__main__':
    main()