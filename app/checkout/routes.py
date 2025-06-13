from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
#from app.auth.dependencies import get_current_user
from app.auth.dependencies import require_user
from app.auth.models import User
from app.cart.models import Cart, CartItem
from app.orders.models import Order, OrderItem

router = APIRouter(prefix="/checkout", tags=["Checkout"])

@router.post("/", summary="Checkout and create order")
def checkout(db: Session = Depends(get_db), current_user: User = Depends(require_user)):
    cart = db.query(Cart).filter(Cart.user_id == current_user.id).first()

    if not cart or not cart.items:
        raise HTTPException(status_code=400, detail="Your cart is empty")

    order = Order(user_id=current_user.id, total_amount=0)
    db.add(order)
    db.flush()

    total = 0
    for item in cart.items:
        order_item = OrderItem(
            order_id=order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price_at_purchase=item.price_at_addition
        )
        total += item.quantity * item.price_at_addition
        db.add(order_item)

    order.total_amount = total

    # Clear cart
    db.query(CartItem).filter(CartItem.cart_id == cart.id).delete()
    db.commit()
    db.refresh(order)

    return {
        "order_id": order.id,
        "total_amount": order.total_amount,
        "message": "Checkout successful. Your order has been placed."
    }
