from datetime import datetime

from models import Order
import commands
from ui_cli.ui_terminal import UiOrderForm, UiOrderFooter

from uuid import UUID


class CliInputHandler:
    def __init__(self, app, order: Order):
        self.app = app
        self.order = order

    def handle_input(self, input_str):
        tokens = input_str.split(' ')  # разделитель - пробел
        if len(tokens) == 1:
            self.exec_cmd(tokens[0].strip())
        elif len(tokens) == 2:
            self.exec_cmd(tokens[0].strip(), tokens[1].strip())
        else:
            raise ValueError("Неправильные данные")

    def exec_cmd(self, cmd, value=None):
        if cmd == "ad":
            self.app.execute(commands.AddProductByPlu(order=self.order, user_input=value, title="Publish the tutorial"))

        elif cmd == "qt":
            self.app.execute(commands.ChangeQty(order=self.order, user_input=value))

        elif cmd == "rs":
            self.app.execute(commands.ResetOrder(order=self.order))

        elif cmd == "st":
            self.app.execute(commands.Storno(order=self.order))

        elif cmd == "sv":
            self.app.execute(commands.SaveOrder(order=self.order))

        else:
            print("Несуществующая команда!")

    def exec(self):
        while True:
            # res = order_form.refresh()
            input_str = input("Enter command (ad, qt, st, rs, sv):")
            if input_str.lower() in ("q", "quit", "exit"):
                break

            try:
                self.handle_input(input_str)
            except ValueError as e:
                print(e)
