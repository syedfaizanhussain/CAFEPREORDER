from flask import Flask, render_template, request, redirect, url_for
import json
# import matplotlib.pyplot as plt
import os
from datetime import datetime 
# import sqlite3


app = Flask(__name__)
ORDER_FILE = 'orders.json'

# Load orders
def load_orders():
    import json
    try:
        with open('orders.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


# Save orders
def save_order(order):
    orders = load_orders()
    orders.insert(0, order)  # newest first
    with open(ORDER_FILE, 'w') as f:
        json.dump(orders[:50], f, indent=4)

# @app.route('/')
# def index():
#     menu = [
#         {'name': 'Pizza', 'price': 150},
#         {'name': 'Pasta', 'price': 120},
#         {'name': 'Burger', 'price': 100},
#         {'name': 'Chai', 'price': 20},
#         {'name': 'Colddrinks', 'price': 30},
#         {'name': 'Ice Cream', 'price': 60},
#         {'name': 'Fries', 'price': 50},
#         {'name': 'Noodles', 'price': 90},
#         {'name': 'Sandwich', 'price': 80},
#         {'name': 'Momos', 'price': 70},
#         {'name': 'Maggi', 'price': 40},
#         {'name': 'Biryani', 'price': 130},
#         {'name': 'Paneer Roll', 'price': 110},
#         {'name': 'Egg Puff', 'price': 25},
#         {'name': 'Veg Puff', 'price': 20},
#         {'name': 'Samosa', 'price': 15},
#         {'name': 'Spring Roll', 'price': 90},
#         {'name': 'Dosa', 'price': 60},
#         {'name': 'Idli', 'price': 30},
#         {'name': 'Vada Pav', 'price': 25}
#     ]
#     return render_template('index.html', menu=menu)
@app.route('/')
def index():
 prices = {
  "Pizza": 80,
  "Pasta": 70,
  "Burger": 60,
  "Chai": 10,
  "Colddrinks": 20,
  "Ice Cream": 30,
  "Fries": 40,
  "Noodles": 50,
  "Sandwich": 35,
  "Momos": 45,
  "Maggi": 25,
  "Biryani": 90,
  "Paneer Roll": 55,
  "Egg Puff": 15,
  "Veg Puff": 15,
  "Samosa": 10,
  "Spring Roll": 50,
  "Dosa": 40,
  "Idli": 30,
  "Vada Pav": 20
 }
 menu = list(prices.keys())# or your own item list
 return render_template("index.html", menu=menu, prices=prices)



# @app.route('/confirm', methods=['POST'])
# def confirm():
#     name = request.form['name']
#     roll = request.form['roll']
#     items = request.form.getlist('items')
#     pickup_time = request.form['pickup_time']
#     order = {
#         'name': name,
#         'roll': roll,
#         'items': items,
#         'pickup_time': pickup_time,
#         'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     }
#     save_order(order)
#     return render_template('confirm.html', single_order=order)

@app.route('/confirm', methods=['POST'])
def confirm():
 name = request.form['name']
 roll = request.form['roll']
 items = request.form.getlist('items')
 pickup_time = request.form['pickup_time']

 prices = {
  "Pizza": 80,
  "Pasta": 70,
  "Burger": 60,
  "Chai": 10,
  "Colddrinks": 20,
  "Ice Cream": 30,
  "Fries": 40,
  "Noodles": 50,
  "Sandwich": 35,
  "Momos": 45,
  "Maggi": 25,
  "Biryani": 90,
  "Paneer Roll": 55,
  "Egg Puff": 15,
  "Veg Puff": 15,
  "Samosa": 10,
  "Spring Roll": 50,
  "Dosa": 40,
  "Idli": 30,
  "Vada Pav": 20
 }

 total_price = sum(prices.get(item, 0) for item in items)

 order = {
 'name': name,
 'roll': roll,
 'items': items,
 'pickup_time': pickup_time,
 'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
 'total_price': total_price
 }

 save_order(order)
 return render_template('confirm.html', single_order=order)

# @app.route('/confirm', methods=['POST'])
# def confirm():
#     name = request.form['name']
#     roll = request.form['roll']
#     items = request.form.getlist('items')
#     pickup_time = request.form['pickup_time']

#     prices = {
#         "Pizza": 80, "Pasta": 70, "Burger": 60, "Chai": 10,
#         "Colddrinks": 20, "Ice Cream": 30, "Fries": 40,
#         "Noodles": 50, "Sandwich": 35, "Momos": 45,
#         "Maggi": 25, "Biryani": 90, "Paneer Roll": 55,
#         "Egg Puff": 15, "Veg Puff": 15, "Samosa": 10,
#         "Spring Roll": 50, "Dosa": 40, "Idli": 30, "Vada Pav": 20
#     }

#     total_price = sum(prices.get(item, 0) for item in items)

#     order = {
#         'name': name,
#         'roll': roll,
#         'items': items,
#         'pickup_time': pickup_time,
#         'total': total_price,
#         'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     }

#     save_order(order)
#     return render_template('confirm.html', single_order=order)


@app.route('/admin')
def admin_login():
    return render_template('admin_login.html')

@app.route('/admin/dashboard', methods=['POST'])
def admin_dashboard():
    password = request.form.get('password')
    if password == "admin123":  # hardcoded password
        orders = load_orders()
        return render_template('admin_dashboard.html', orders=orders)
    else:
        return "<h3>Unauthorized Access</h3>"
# @app.route('/admin/dashboard')
# def admin_dashboard():
#     conn = sqlite3.connect('orders.db')
#     conn.row_factory = sqlite3.Row
#     cursor = conn.cursor()
    
#     cursor.execute("SELECT * FROM orders")
#     orders = cursor.fetchall()
#     conn.close()

#     return render_template('admin_dashboard.html', orders=orders)


@app.route('/admin/history')
def order_history():
    orders = load_orders()
    return render_template('order_history.html', orders=orders)

if __name__ == '__main__':
    app.run(debug=True)
