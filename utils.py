def load_orders():
    import json
    with open('orders.json', 'r') as f:
        return json.load(f)
