```markdown
# 🧠 Django Authentication System — BlogSite Project

This project is a **Django-based authentication system** that includes user registration, login, logout, and password reset via **email OTP verification**.  
It uses **SQLite3** as the default database and is designed to be modular and easily extendable for future phases (like blog creation and user dashboard).

---

## 🚀 Features Implemented (Phase 3)

### ✅ **User Authentication System**
- User Registration  
- User Login / Logout  
- Redirects to `home.html` only after successful login  
- Unauthorized users are redirected to the login page  

### 🔐 **Password Reset via Email OTP**
- Users can reset their password using their registered email  
- OTP is sent using SMTP (Gmail configuration)  
- Users can verify OTP and reset password securely  

### 🗂️ **Database**
- Switched from MongoDB to **SQLite3** for simplicity  
- All authentication data stored in `db.sqlite3`

---

## 🏗️ Project Structure

```

BlogSite/
├── blogsite/
│   ├── accounts/
│   │   ├── migrations/
│   │   ├── templates/
│   │   │   └── accounts/
│   │   │       ├── login.html
│   │   │       ├── register.html
│   │   │       ├── home.html
│   │   │       ├── password_reset_request.html
│   │   │       └── password_reset_confirm.html
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── forms.py
│   │   └── models.py
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── db.sqlite3
├── manage.py
└── README.md

````

---

## ⚙️ Installation & Setup

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/BlogSite.git
cd BlogSite
````

### **2️⃣ Create & Activate Virtual Environment**

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Mac/Linux
```

### **3️⃣ Install Dependencies**

```bash
pip install django
```

### **4️⃣ Run Migrations**

```bash
python manage.py migrate
```

### **5️⃣ Create Superuser (Optional)**

```bash
python manage.py createsuperuser
```

### **6️⃣ Run the Server**

```bash
python manage.py runserver
```

Then open:
👉 **[http://127.0.0.1:8000/login/](http://127.0.0.1:8000/login/)**

---

## ✉️ Email Configuration (For Password Reset)

Edit your `settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_16_char_app_password'
```

> ⚠️ **Important:**
>
> * Enable **2-Step Verification** in your Google Account.
> * Generate an **App Password** under “Security → App Passwords” and use it as `EMAIL_HOST_PASSWORD`.

---

## 🧑‍💻 Current Views

| View Name                     | URL Path                  | Description                         |
| ----------------------------- | ------------------------- | ----------------------------------- |
| `login_view`                  | `/login/`                 | Login page with reset password link |
| `register_view`               | `/register/`              | User registration page              |
| `home_view`                   | `/home/`                  | Dashboard (login required)          |
| `password_reset_request_view` | `/password-reset/`        | Request OTP via email               |
| `password_reset_verify_view`  | `/password-reset-verify/` | Verify OTP and set new password     |

---

## 🧱 Next Phase (Planned)

**Phase 4: Blog Module**

* Add CRUD operations for blog posts
* Integrate user-based post ownership
* Use Django Models & Forms for content management
* Add post listing on home page

---

## 🧾 License

This project is for educational purposes and open-source development practice.
You’re free to modify and extend it.

---

## 👨‍💻 Developer

**Sayan Banerjee**
Machine Learning & Backend Developer
📧 [banerjeesayan554@gmail.com](mailto:banerjeesayan554@gmail.com)

---

```

---

Would you like me to include the **Gmail App Password setup guide (with screenshots and step-by-step instructions)** in this same file so beginners can configure it easily?
```
