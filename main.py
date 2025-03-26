from datetime import datetime

from models import Order
import commands
from ui_cli.ui_terminal import UiOrderForm, UiOrderFooter
from app import create_app

from uuid import UUID

app = create_app()
order = Order(UUID(int=1))


def parse_cmd(input_str):
    tokens = input_str.split(' ')  #  разделитель - пробел
    if len(tokens) == 1:
        handle_cmd(tokens[0].strip())
    elif len(tokens) == 2:
        handle_cmd(tokens[0].strip(), tokens[1].strip())
    else:
        raise ValueError("Неправильные данные")

def handle_cmd(cmd, value=None):
    if cmd == "ad":
        # plu = int(value)
        # order.add_line(plu)
        app.execute(commands.AddProductByPlu(order=order, user_input=value, title="Publish the tutorial"))

    elif cmd == "qt":
        app.execute(commands.ChangeQty(order=order, user_input=value))

    elif cmd == "rs":
        app.execute(commands.ResetOrder(order=order))

    elif cmd == "st":
        app.execute(commands.Storno(order=order))

    elif cmd == "sv":
        app.execute(commands.SaveOrder(order=order))

    else:
        print("Несуществующая команда!")


    # app.execute(commands.SaveOrder(order=order))


def main():

    order_form = UiOrderForm(order)
    order_footer = UiOrderFooter(order)
    while True:
        # res = order_form.refresh()
        input_str = input("Enter command (ad, qt, st, rs, sv):")
        if input_str.lower() in ("q", "quit", "exit"):
            break

        try:
            parse_cmd(input_str)
        except ValueError as e:
            print(e)


if __name__ == '__main__':
    main()