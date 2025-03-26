from collections.abc import Callable
from datetime import datetime
from typing import Any

from lato import Application, TransactionContext

from models import Order
from order_repo import OrderRepository
from order_module import orders
import commands
from ui_terminal import UiOrderForm, UiOrderFooter

from uuid import UUID


def create_app() -> Application:
    # create an application with dependencies used across the handlers
    app = Application(
        "Tutorial",
        order_repository=OrderRepository(),  # used by todos module
        # notification_service=NotificationService(),  # used by notifications module
    )
    # add modules to the app
    app.include_submodule(orders)
    # app.include_submodule(notifications)

    # add transaction context middlewares
    @app.on_enter_transaction_context
    def on_enter_transaction_context(ctx: TransactionContext):
        print("Begin transaction")
        # ctx.set_dependencies(
        #     now=datetime.now(),
        # )

    @app.on_exit_transaction_context
    def on_exit_transaction_context(ctx: TransactionContext, exception=None):
        print("End transaction")

    @app.transaction_middleware
    def logging_middleware(ctx: TransactionContext, call_next: Callable) -> Any:
        handler = ctx.current_handler
        message_name = ctx.get_dependency("message").__class__.__name__
        handler_name = f"{handler.source}.{handler.fn.__name__}"
        print(f"Executing {handler_name}({message_name})")
        result = call_next()
        print(f"Result from {handler_name}: {result}")
        return result

    # @app.transaction_middleware
    # def analytics_middleware(ctx: TransactionContext, call_next: Callable) -> Any:
    #     result = call_next()
    #     todos_counter = ctx.get_dependency(TodosCounter)
    #     print(
    #         f" todos stats: {todos_counter.completed_todos}/{todos_counter.created_todos}"
    #     )
    #     return result

    return app

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