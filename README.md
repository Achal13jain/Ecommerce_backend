<div align="center">

# 🛒 E-commerce Backend API

### FastAPI-powered RESTful backend with JWT authentication, product management, and order processing

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-316192.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

[Features](#features) • [Tech Stack](#tech-stack) • [Getting Started](#getting-started) • [API Documentation](#api-documentation) • [Project Structure](#project-structure)

</div>

---

## 📋 Overview

A production-ready e-commerce backend system built with FastAPI that provides secure user authentication, comprehensive product management, shopping cart functionality, and order processing capabilities. Designed with scalability, security, and modularity at its core.

### 🎯 Key Highlights

- **Secure Authentication**: JWT-based authentication with OAuth2 password flow and bcrypt password hashing
- **Role-Based Access Control**: Separate admin and user permissions for resource management
- **Complete E-commerce Flow**: From product browsing to order placement
- **Database Migrations**: Alembic integration for seamless schema versioning
- **RESTful API Design**: Clean, intuitive endpoints following REST conventions

---

## ✨ Features

### 🔐 Authentication & Authorization
- User registration and login with hashed password storage
- JWT access token generation and validation
- Protected routes with role-based access control

### 📦 Product Management
- Full CRUD operations for products (admin only)
- Public product catalog with search and filtering capabilities
- Detailed product information retrieval

### 🛒 Shopping Cart
- Add, update, and remove cart items
- Price tracking at time of addition
- Persistent cart across sessions

### 📊 Order Processing
- Place orders directly from cart
- Order status tracking and history
- User-specific order management
---

## 🛠 Tech Stack

| Component | Technology |
|-----------|-----------|
| **Framework** | [FastAPI](https://fastapi.tiangolo.com/) |
| **Database** | [PostgreSQL](https://www.postgresql.org/) |
| **ORM** | [SQLAlchemy](https://www.sqlalchemy.org/) |
| **Authentication** | JWT + OAuth2 |
| **Password Hashing** | Passlib (bcrypt) |
| **Migrations** | [Alembic](https://alembic.sqlalchemy.org/) |
| **Configuration** | Pydantic Settings |
| **Environment** | Python 3.9+ Virtual Environment |

---

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.9 or higher
- PostgreSQL 12 or higher
- pip (Python package manager)
- virtualenv or venv

### Installation

1. **Clone the repository**
```
git clone https://github.com/Achal13jain/Ecommerce_backend.git
cd Ecommerce_backend
```

2. **Create and activate virtual environment**

Windows

```
python -m venv venv
venv\Scripts\activate
```
Linux/MacOS
```
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```
pip install -r requirements.txt
```

4. **Configure environment variables**

Create a `.env` file in the root directory:
```
DATABASE_URL=postgresql://username:password@localhost:5432/ecommerce_db
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```


5. **Initialize database**

Create database
```
createdb ecommerce_db
```
Run migrations
```
alembic upgrade head
```

6. **Run the application**
```
uvicorn app.main:app --reload
```
The API will be available at `http://localhost:8000`.

---

## 📚 API Documentation

Once the server is running, access the interactive API documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### 🔑 Core Endpoints

#### Authentication
- `POST /auth/signup` - Register new user
- `POST /auth/signin` - User login (returns JWT token)

#### Products
- `GET /products` - List all products (public)
- `GET /products/{id}` - Get product details (public)
- `POST /products` - Create product (admin only)
- `PUT /products/{id}` - Update product (admin only)
- `DELETE /products/{id}` - Delete product (admin only)

#### Cart
- `GET /cart` - View cart items
- `POST /cart` - Add item to cart
- `PUT /cart/{id}` - Update cart item quantity
- `DELETE /cart/{id}` - Remove item from cart

#### Orders
- `POST /orders` - Place order from cart
- `GET /orders` - View order history
- `GET /orders/{id}` - Get order details

---

## 📂 Project Structure
```
Ecommerce_backend/
├── app/
│ ├── init.py
│ ├── main.py # Application entry point
│ ├── config.py # Configuration settings
│ ├── database.py # Database connection
│ ├── models/ # SQLAlchemy models
│ │ ├── user.py
│ │ ├── product.py
│ │ ├── cart.py
│ │ └── order.py
│ ├── schemas/ # Pydantic schemas
│ │ ├── user.py
│ │ ├── product.py
│ │ ├── cart.py
│ │ └── order.py
│ ├── routers/ # API route handlers
│ │ ├── auth.py
│ │ ├── products.py
│ │ ├── cart.py
│ │ └── orders.py
│ └── utils/ # Utility functions
│ ├── auth.py # JWT & password hashing
│ └── dependencies.py # Dependency injection
├── alembic/ # Database migrations
│ ├── versions/
│ └── env.py
├── tests/ # Unit and integration tests
├── .env.example # Environment variables template
├── .gitignore
├── alembic.ini # Alembic configuration
├── requirements.txt # Python dependencies
└── README.md
```
---

## 🔒 Security Features

- Password hashing using bcrypt algorithm
- JWT token-based authentication with expiration
- Protected routes with dependency injection
- SQL injection prevention via SQLAlchemy ORM
- Environment-based configuration management

---

## 🚀 Future Enhancements

- [ ] Payment gateway integration (Stripe/PayPal)
- [ ] Email notification system
- [ ] Product image upload and storage
- [ ] Advanced filtering and search
- [ ] Rate limiting and throttling
- [ ] Redis caching layer
- [ ] Docker containerization
- [ ] CI/CD pipeline setup

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please ensure your code follows the existing style and includes appropriate tests.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Achal Jain**

- GitHub: [@Achal13jain](https://github.com/Achal13jain)
- Repository: [Ecommerce_backend](https://github.com/Achal13jain/Ecommerce_backend)

---

## 🙏 Acknowledgments

- FastAPI documentation and community
- SQLAlchemy ORM framework
- JWT authentication best practices

---

<div align="center">

### ⭐ Star this repository if you find it helpful!


</div>