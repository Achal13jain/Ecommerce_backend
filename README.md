# E-commerce Backend

A fully functional **e-commerce backend system** built using **FastAPI**, providing features like user authentication, admin product management, public product browsing, cart handling, and order placement.

## Features

- **User Authentication**
  - Signup / Signin with hashed passwords
  - JWT-based access token handling
-  **Admin Product Management**
  - CRUD operations on products
  - Admin-only access control
-  **Cart System**
  - Add/remove/update cart items
  - Track prices at time of addition
-  **Order Management**
  - Place orders from cart
  - Track order status
-  **Public Product Browsing**
  - Filter/search products
  - View product details
-  **Secure, Modular, and Scalable**

##  Tech Stack

| Layer           | Tech                    |  
|----------------|--------------------------|
| Framework      | FastAPI                  |
| Database       | PostgreSQL               |
| ORM            | SQLAlchemy               |
| Auth           | JWT + OAuth2             |
| Password Hash  | Passlib (bcrypt)         |
| Migrations     | Alembic                  |
| Settings       | Pydantic BaseSettings    |
| Environment    | Python Virtual Env (`venv`) |