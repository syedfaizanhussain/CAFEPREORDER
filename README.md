# CAFEPREORDER
Cafepreorder is a web application that allows students or employees to pre-order food items from college canteen. It streamlines the ordering process and avoids long queues.

**CafePreorder** is a lightweight web app built using **Python Flask** that allows students to **pre-order food** and lets administrators **view all orders** through a secure login panel. The orders are stored in a simple `JSON` file for ease of use, making it beginner-friendly and perfect for hackathons or small-scale canteen automation.



## 🚀 Features

- ✅ Students can select food items and place orders with name, roll number, and pickup time.
- ✅ All orders are saved in a `orders.json` file (no database needed).
- ✅ Admin login panel (`/admin`) to view live orders securely.
- ✅ Admin can also view full order history (`/admin/history`).
- ✅ Clean and responsive UI built using HTML + basic CSS.


## 🛠️ Technologies Used

- **Python 3.x**
- **Flask**
- **HTML / CSS**
- **JSON** for data storage


## ⚙️ Project Structure
canteenpreorder/
├── app.py
├── orders.json
├── templates/
│ ├── index.html
│ ├── confirm.html
│ ├── admin_login.html
│ ├── admin_dashboard.html
│ └── order_history.html
└── static/
└── 
## Install dependencies 
    python app.py


## 🔐 Admin Panel
Visit: http://127.0.0.1:5000/admin

Default Password: 'admin123'


## 💡 Ideas for Future Improvements
Add SQLite or MongoDB for better data handling.

OTP verification via email/SMS.

Add item images and category filtering.

Export reports as Excel/PDF.


##👨‍💻 Developed By
 Syed Faizan Hussain
 Mohd Abdul Parvez
 Mohd Rizwan
Aspiring IT Engineer | Hackathon Explorer 🚀
