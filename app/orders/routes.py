from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.auth.dependencies import require_user
from app.auth.dependencies import get_current_user
from app.orders import models, schemas
from app.cart.models import Cart, CartItem
from app.auth.models import User
from fastapi import status
router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/", response_model=schemas.OrderOut)
def create_order(db: Session = Depends(get_db), current_user: User = Depends(require_user)):
    # Fetch the user's cart
    cart = db.query(Cart).filter(Cart.user_id == current_user.id).first()
    if not cart or not cart.items:
        raise HTTPException(status_code=400, detail="Your cart is empty")

    # Create the order
    order = models.Order(user_id=current_user.id, total_amount=0)
    db.add(order)
    db.flush()  # Get order.id without committing yet

    total_amount = 0
    for item in cart.items:
        order_item = models.OrderItem(
            order_id=order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price_at_purchase=item.price_at_addition
        )
        db.add(order_item)
        total_amount += item.quantity * item.price_at_addition

    order.total_amount = total_amount

    # Clear cart
    db.query(CartItem).filter(CartItem.cart_id == cart.id).delete()

    db.commit()
    db.refresh(order)
    return order


@router.get("/", response_model=list[schemas.OrderOut])
def list_my_orders(db: Session = Depends(get_db), current_user: User = Depends(require_user)):
    return db.query(models.Order).filter(models.Order.user_id == current_user.id).all()

# @router.get("/admin", response_model=list[schemas.OrderOut], status_code=status.HTTP_200_OK)
# def list_all_orders_admin(
#     db: Session = Depends(get_db),
#     current_user: User = Depends(get_current_user)
# ):
#     if not current_user.is_admin:
#         raise HTTPException(status_code=403, detail="Not authorized to view all orders")

#     return db.query(models.Order).all()

@router.get("/{order_id}", response_model=schemas.OrderOut)
def get_order_detail(order_id: int, db: Session = Depends(get_db), current_user: User = Depends(require_user)):
    order = db.query(models.Order).filter(models.Order.id == order_id, models.Order.user_id == current_user.id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


