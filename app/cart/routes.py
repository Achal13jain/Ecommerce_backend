from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.cart import models, schemas
from app.products.models import Product
from app.core.database import get_db
# from app.auth.dependencies import get_current_user
from app.auth.models import User
from app.auth.dependencies import require_user

router = APIRouter(prefix="/cart", tags=["Cart"])

@router.post("/", response_model=schemas.CartOut)
def add_to_cart(request: schemas.AddToCartRequest, db: Session = Depends(get_db), current_user: User = Depends(require_user)):
    cart = db.query(models.Cart).filter(models.Cart.user_id == current_user.id).first()
    if not cart:
        cart = models.Cart(user_id=current_user.id)
        db.add(cart)
        db.commit()
        db.refresh(cart)

    for item in request.items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        if not product:
            raise HTTPException(status_code=404, detail=f"Product with ID {item.product_id} not found")

        cart_item = db.query(models.CartItem).filter_by(cart_id=cart.id, product_id=item.product_id).first()
        if cart_item:
            cart_item.quantity += item.quantity
        else:
            cart_item = models.CartItem(
                cart_id=cart.id,
                product_id=item.product_id,
                quantity=item.quantity,
                price_at_addition=product.price
            )
            db.add(cart_item)

    db.commit()
    db.refresh(cart)
    return cart


@router.get("/", response_model=schemas.CartOut)
def get_my_cart(db: Session = Depends(get_db), current_user: User = Depends(require_user)):
    cart = db.query(models.Cart).filter(models.Cart.user_id == current_user.id).first()
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")
    return cart


@router.patch("/{item_id}", response_model=schemas.CartOut)
def update_cart_item(item_id: int, quantity: int, db: Session = Depends(get_db), current_user: User = Depends(require_user)):
    cart = db.query(models.Cart).filter(models.Cart.user_id == current_user.id).first()
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")

    item = db.query(models.CartItem).filter_by(id=item_id, cart_id=cart.id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found in your cart")

    if quantity <= 0:
        db.delete(item)
    else:
        item.quantity = quantity

    db.commit()
    db.refresh(cart)
    return cart


@router.delete("/{item_id}", status_code=204)
def delete_cart_item(item_id: int, db: Session = Depends(get_db), current_user: User = Depends(require_user)):
    cart = db.query(models.Cart).filter(models.Cart.user_id == current_user.id).first()
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")

    item = db.query(models.CartItem).filter_by(id=item_id, cart_id=cart.id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found in your cart")

    db.delete(item)
    db.commit()
