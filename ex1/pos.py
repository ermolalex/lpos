from mopyx import model, render, render_call, action

from ui_cli.order_form import UiOrderForm, UiOrderFooter
from models import Order
from db import search

order = Order()

# class OrderForm(QWidget, Ui_Form):
#     def __init__(self) -> None:
#         super(OrderForm, self).__init__()
#
#         self.setupUi(self)
#
#         self.btn_add.clicked.connect(self.add_item)
#         self.btn_change_qty.clicked.connect(self.change_qty)
#         self.btn_cancel.clicked.connect(self.cancel_order)
#
#         # виджеты, добавленные вручную
#         self.btn_set_prod = QPushButton("set product")
#         self.verticalLayout_2.addWidget(self.btn_set_prod)
#         self.btn_set_prod.clicked.connect(self.set_product)
#
#         self.btn_open_sub = QPushButton("Open Sub")
#         self.verticalLayout_2.addWidget(self.btn_open_sub)
#         self.btn_open_sub.clicked.connect(self.open_sub)
#
#
#         self.show()
#
#         self.update_from_model()
#
#     @render
#     def update_from_model(self):
#         render_call(
#             lambda: self.label_total.setText(
#                 f"Итого: {order.total}"))
#         self.update_table()
#         self.update_buttons()
#
#     @render(ignore_updates=True)
#     def update_table(self):
#         items = order.items
#         self.tableWidget.setRowCount(len(items))
#         self.tableWidget.setColumnCount(3)
#
#         for i, item in enumerate(items):
#             self.tableWidget.setItem(i, 0, QTableWidgetItem(item.name))
#             self.tableWidget.setItem(i, 1, QTableWidgetItem(str(item.unit_price)))
#             self.tableWidget.setItem(i, 2, QTableWidgetItem(str(item.qty)))
#
#         render_call(lambda: self.tableWidget.selectRow(order.selectedItemIndex),
#                     ignore_updates=True)
#
#
#     @render(ignore_updates=True)
#     def update_buttons(self):
#         self.btn_change_qty.setEnabled(order.selectedItemIndex >= 0)
#         self.btn_cancel.setEnabled(len(order.items) > 0)
#
#     @action
#     def set_selected_item_index(self):
#         order.selectedItemIndex = self.tableWidget.currentRow()
#
#     def add_item(self):
#         plu = int(self.lineEdit.text())
#         if plu:
#             current_line = order.add_line(plu)
#             print(f"добавлен товар")
#
#         self.lineEdit.setText("")
#         return
#
#     #@action
#     def change_qty(self):
#         qty = int(self.lineEdit.text())
#         if qty:
#             item = order.items[order.selectedItemIndex]
#             item.qty = qty
#             order.items[order.selectedItemIndex] = item
#
#     def cancel_order(self):
#         order.items = []
#
#     def set_product(self):
#         curr_index = order.selectedItemIndex
#         item = order.items[curr_index]
#         print(item.item_total)
#
#     def open_sub(self):
#         sub_form = SubForm(order)
#         sub_form.setModal(False)
#         sub_form.show()




def parse_cmd(input_str):
    tokens = input_str.split(' ')  #  разделитель - пробел
    if len(tokens) == 1:
        handle_cmd(tokens[0])
    elif len(tokens) == 2:
        handle_cmd(tokens[0], tokens[1])
    else:
        raise ValueError("Incorrect input")

def handle_cmd(cmd, value=None):
    if cmd == "ad":
        plu = int(value)
        order.add_line(plu)

    elif cmd == "qt":
        qty = int(value)
        if not order.has_items():
            print("No items in order")
            return

        index = order.length() - 1
        order.items[index].qty = qty

    elif cmd == "st":
        order.items.pop()

def main():
    order_form = UiOrderForm(order)
    order_footer = UiOrderFooter(order)
    while True:
        # res = order_form.refresh()
        input_str = input("Enter command (ad, qt, st):")
        if input_str.lower() in ("q", "quit", "exit"):
            break
        parse_cmd(input_str)


if __name__ == '__main__':
    main()
