from datetime import datetime

from models import Order
import commands
from ui_cli.ui_terminal import UiOrderForm, UiOrderFooter
from ui_cli.input_handler import CliInputHandler
from app import create_app

from uuid import UUID

app = create_app()
order = Order(UUID(int=1))


def main():

    order_form = UiOrderForm(order)
    order_footer = UiOrderFooter(order)

    input_handler = CliInputHandler(app, order)
    input_handler.exec()


if __name__ == '__main__':
    main()