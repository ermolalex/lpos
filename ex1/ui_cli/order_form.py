from mopyx import render
from prettytable import PrettyTable

from models import Order


class UiOrderForm():
    def __init__(self, order: Order):
        self.order = order
        self.table = PrettyTable()

        self.refresh()

    @render
    def refresh(self):
        self.table.clear()

        self.table.field_names = ["Prod", "Qty", "Unit price", "Price"]
        for item in self.order.items:
            self.table.add_row(
                [
                    item.name,
                    item.qty,
                    item.unit_price,
                    item.item_total
                ]
            )

        print(self.table)
        # self.cmd = input("Введите следующую команду:")
        #
        # return self.cmd

class UiOrderFooter():
    def __init__(self, order: Order):
        self.order = order

        self.refresh()

    @render
    def refresh(self):
        print(f"Order Total: {self.order.total}")
