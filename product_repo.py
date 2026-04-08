class ProductRepository:
    def __init__(self):
        self._products = {}

    def add(self, product):
        self._products[product.id] = product

    def get(self, product_id):
        return self._products.get(product_id)

    def list_all(self):
        return list(self._products.values())