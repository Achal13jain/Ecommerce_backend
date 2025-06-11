# ecommerce-fastapi-backend
# 🛍️ E-commerce Backend System using FastAPI

This project is a **secure, modular, and production-ready backend REST API** for an e-commerce platform. It supports:

- 🧑‍💼 Admin product management (CRUD)
- 🧾 Auth (Signup, Signin)
- 🔍 Product listing, filtering, search
- 🛒 Cart management
- 💳 Dummy checkout and order management

---

## 📦 Features
- Role-based access control (RBAC)
- JWT Auth (Access + Refresh Tokens)
- SQLAlchemy ORM + PostgreSQL (or SQLite)
- Clean modular structure
- Pydantic validation
- Swagger UI docs at `/docs`

---

## 🚀 Getting Started

### 1️⃣ Clone and install dependencies

```bash
git clone https://github.com/yourname/ecommerce_fastapi.git
cd ecommerce_fastapi
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows
pip install -r requirements.txt
