from lato import ApplicationModule, TransactionContext
from mopyx import action

from models import Order, Item
from commands import ResetOrder, AddProductByPlu, ChangeQty, Storno, SaveOrder
from events import OrderSaved
from order_repo import OrderRepository
from db import search

orders = ApplicationModule("orders")

@orders.handler(ResetOrder)
def handle_reset_order(cmd: ResetOrder):
    order = cmd.order
    order.reset()


@action
@orders.handler(AddProductByPlu)
def handle_add_product_by_plu(cmd: AddProductByPlu):
    order = cmd.order

    try:
        plu = int(cmd.user_input)
    except ValueError:
        raise ValueError(f"Неправильный PLU: {cmd.user_input}")


    prod = search(plu)
    if prod is None:
        print(f"Товар с кодом {plu} не найден!")
        return

    item = Item(
        name=prod['name'],
        unit_price=prod['unit_price'],
    )
    order.items.append(item)

@orders.handler(ChangeQty)
def handle_change_qty(cmd: ChangeQty):
    order = cmd.order
    index = cmd.index

    if not order.has_items():
        print("No items in order")
        return

    try:
        qty = int(cmd.user_input)
    except ValueError:
        raise ValueError(f"Неправильное количество: {cmd.user_input}")

    if index is None:
        index = len(order.items) - 1

    order.items[index].qty = qty

# @todos.handler(GetSomeTodos)
# def get_some_todos(query: GetSomeTodos, repo: TodoRepository, now: datetime):
#     if query.completed is None:
#         result = repo.get_all()
#     else:
#         result = (
#             repo.get_all_completed()
#             if query.completed
#             else repo.get_all_not_completed()
#         )
#
#     return [todo_model_to_read_model(todo, now) for todo in result]
#
# def todo_model_to_read_model(todo: TodoModel, now: datetime) -> TodoReadModel:
#     return TodoReadModel(
#         id=todo.id,
#         title=todo.title,
#         description=todo.description,
#         is_due=todo.is_due(now),
#         is_completed=todo.is_completed,
#     )
#

@orders.handler(Storno)
def handle_storno(cmd: AddProductByPlu):
    order = cmd.order

    if not order.has_items():
        print("No items in order")
        return

    order.items.pop()


@orders.handler(SaveOrder)
def handle_save(cmd: SaveOrder, repo: OrderRepository, ctx: TransactionContext):
    order = cmd.order
    if not order.has_items():
        print("Order is empty")
        return
    repo.add(order)
    ctx.publish(OrderSaved(order=order))

