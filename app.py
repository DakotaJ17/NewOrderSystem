from flask import Flask, jsonify, abort
from Domain.models import Product, Order
from Repository.product_repo import ProductRepository
from Repository.order_repo import OrderRepository
from Service.order_service import OrderService

app = Flask(__name__)

# --- Initialization ---
p_repo = ProductRepository()
o_repo = OrderRepository()
service = OrderService(p_repo, o_repo)

# --- Seed Data (As per Iteration 4 requirements) ---
def startup_data():
    # Adding products to the repo
    p_repo.add_product(Product(1, "Mug", 12.50))
    p_repo.add_product(Product(2, "Scarf", 25.00))

def startup_order():
    # Creating the initial seed order via the Service
    # Note: We convert the dicts from your assignment into the tuple format 
    # our Service expects: (id, quantity)
    items_raw = [
        {"id": 1, "qty": 2},
        {"id": 2, "qty": 1}
    ]
    formatted_items = [(item["id"], item["qty"]) for item in items_raw]
    service.create_order(formatted_items)

# Run the seeds
startup_data()
startup_order()

# --- Endpoints ---

@app.route('/products', methods=['GET'])
def get_products():
    # Retrieve all products and convert them to a list of dicts for JSON
    all_products = p_repo.get_all() 
    return jsonify([p.__dict__ for p in all_products])

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    # Find the order
    order = o_repo.get_by_id(order_id)
    
    if not order:
        # Return a 404 error if not found
        abort(404, description="Order not found")

    # Construct the response with the list of items and the total
    return jsonify({
        "order_id": order.id,
        "items": order.items, # This assumes your Order model stores item details
        "total": order.total_price
    })

if __name__ == '__main__':
    # Start the server
    app.run(debug=True, port=5000)
