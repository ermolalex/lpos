import sys

from PySide6.QtWidgets import *
from mopyx import model, render, render_call, action

from ui_qt.order_form_ui import Ui_Form
from models import Order
from db import search

order = Order()

class OrderForm(QWidget, Ui_Form):
    def __init__(self) -> None:
        super(OrderForm, self).__init__()

        self.setupUi(self)

        self.btn_add.clicked.connect(self.add_item)
        self.btn_change_qty.clicked.connect(self.change_qty)
        self.btn_cancel.clicked.connect(self.cancel_order)

        # виджеты, добавленные вручную
        self.btn_set_prod = QPushButton("set product")
        self.verticalLayout_2.addWidget(self.btn_set_prod)
        self.btn_set_prod.clicked.connect(self.set_product)

        self.btn_open_sub = QPushButton("Open Sub")
        self.verticalLayout_2.addWidget(self.btn_open_sub)
        self.btn_open_sub.clicked.connect(self.open_sub)


        self.show()

        self.update_from_model()

    @render
    def update_from_model(self):
        render_call(
            lambda: self.label_total.setText(
                f"Итого: {order.total}"))
        self.update_table()
        self.update_buttons()

    @render(ignore_updates=True)
    def update_table(self):
        items = order.items
        self.tableWidget.setRowCount(len(items))
        self.tableWidget.setColumnCount(3)

        for i, item in enumerate(items):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(item.name))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(item.unit_price)))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(item.qty)))

        render_call(lambda: self.tableWidget.selectRow(order.selectedItemIndex),
                    ignore_updates=True)


    @render(ignore_updates=True)
    def update_buttons(self):
        self.btn_change_qty.setEnabled(order.selectedItemIndex >= 0)
        self.btn_cancel.setEnabled(len(order.items) > 0)

    @action
    def set_selected_item_index(self):
        order.selectedItemIndex = self.tableWidget.currentRow()

    def add_item(self):
        plu = int(self.lineEdit.text())
        if plu:
            current_line = order.add_line(plu)
            print(f"добавлен товар")

        self.lineEdit.setText("")
        return

    #@action
    def change_qty(self):
        qty = int(self.lineEdit.text())
        if qty:
            item = order.items[order.selectedItemIndex]
            item.qty = qty
            order.items[order.selectedItemIndex] = item

    def cancel_order(self):
        order.items = []

    def set_product(self):
        curr_index = order.selectedItemIndex
        item = order.items[curr_index]
        print(item.item_total)

    def open_sub(self):
        sub_form = SubForm(order)
        sub_form.setModal(False)
        sub_form.show()

def main():
    app = QApplication(sys.argv)
    of = OrderForm()

    ret = app.exec_()
    sys.exit(ret)


if __name__ == '__main__':
    main()
