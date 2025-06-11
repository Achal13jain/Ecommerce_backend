from fastapi import FastAPI
from app.auth.routes import router as auth_router
from app.products import routes as product_routes
from app.products.routes import public_router
from app.cart import routes as cart_routes
from app.orders.routes import router as orders_router

from app.auth import models as auth_models
from app.orders import models as order_models
from app.checkout.routes import router as checkout_router
app = FastAPI(
    title="E-commerce Backend API",
    description="A backend system for product management, user authentication, and orders using FastAPI.",
    version="1.0.0"
)

# Include authentication routes
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(product_routes.router)
app.include_router(public_router)
app.include_router(cart_routes.router)
app.include_router(orders_router)
app.include_router(checkout_router) 

# Health check route
@app.get("/")
def root():
    return {"message": "E-commerce API is running"}