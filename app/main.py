from fastapi import FastAPI, Request
from app.core.logger import logger     
from fastapi.responses import JSONResponse
from app.auth.routes import router as auth_router
from app.products import routes as product_routes
from app.products.routes import public_router
from app.cart import routes as cart_routes
from app.orders.routes import router as orders_router

from app.auth import models as auth_models
from app.orders import models as order_models
from app.checkout.routes import router as checkout_router

#Instantiate the application 
app = FastAPI(
    title="E-commerce Backend API",
    description="A backend system for product management, user authentication, and orders using FastAPI.",
    version="1.0.0"
)
@app.middleware("http")
async def access_log_middleware(request: Request, call_next):
    ip = request.client.host
    method = request.method
    path = request.url.path
    logger.info(f"{ip} -> {method} {path}")
    try:
        response = await call_next(request)
        return response
    except Exception as exc:
        logger.exception("Unhandled exception")
        # Ensure uniform error payload per SRS
        return JSONResponse(
            status_code=500,
            content={"error": True, "message": "Internal Server Error", "code": 500},
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