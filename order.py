from domain.order_item import OrderItem

class Order:
    def __init__(self, order_id):
        self.id = order_id
        self.items = []

    def add_item(self, product, quantity):
        self.items.append(OrderItem(product, quantity))

    def calculate_total(self):
        return sum(item.get_subtotal() for item in self.items)