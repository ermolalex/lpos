from uuid import UUID
from models import Order

class OrderRepository:

    def __init__(self):
        self.orders: list[Order] = []

    def add(self, order: Order) -> None:
        self.orders.append(order)

    def get_by_id(self, order_id: UUID) -> Order:
        for order in self.orders:
            if order.id == order_id:
                return order
        raise ValueError(f"Order with id {order_id} does not exist")

    def get_all(self) -> list[Order]:
        return self.orders

