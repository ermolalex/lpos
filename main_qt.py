import sys
from uuid import UUID

from PySide6.QtWidgets import *
from mopyx import model, render, render_call, action

from ui_qt.order_form import OrderForm
from models import Order
from app import create_app

app = create_app()
order = Order(UUID(int=1))


def main():
    q_app = QApplication(sys.argv)
    of = OrderForm(app, order)

    ret = q_app.exec()
    sys.exit(ret)


if __name__ == '__main__':
    main()
