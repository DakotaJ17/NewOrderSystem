from domain.product import Product
from domain.order import Order
from repository.product_repo import ProductRepository
from repository.order_repo import OrderRepository


def main():
    # Setup
    p_repo = ProductRepository()
    o_repo = OrderRepository()

    # Add Products to Repo
    p_repo.add(Product(1, "Mug", 12.50))
    p_repo.add(Product(2, "Scarf", 25.00))

    # Create Order using Repo data
    new_order = Order(101)
    new_order.add_item(p_repo.get(1), 2)  # 2 Mugs
    new_order.add_item(p_repo.get(2), 1)  # 1 Scarf

    # Save Order
    o_repo.save(new_order)

    # Print Results
    saved_order = o_repo.get(101)
    for item in saved_order.items:
        print(f"Item: {item.product.name} x{item.quantity} = ${item.get_subtotal():.2f}")

    print(f"Total = ${saved_order.calculate_total():.2f}")


if __name__ == "__main__":
    main()