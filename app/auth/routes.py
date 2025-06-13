from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.auth import models, schemas, utils
from app.core.database import SessionLocal
from app.auth.dependencies import get_current_user, require_admin
from app.auth.models import User
router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/signup", response_model=schemas.UserOut, status_code=status.HTTP_201_CREATED)
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check if email already exists
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash the password
    hashed_pw = utils.hash_password(user.password)

    # Create new user
    new_user = models.User(
        name=user.name,
        email=user.email,
        hashed_password=hashed_pw,
        role=user.role,
        is_admin=True if user.role == "admin" else False  # ✅ Derive is_admin flag
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
from app.auth.jwt_handler import create_access_token, create_refresh_token
from app.auth.schemas import UserLogin

@router.post("/signin")
def signin(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    if not utils.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(data={"user_id": db_user.id})

    refresh_token = create_refresh_token(data={"sub": db_user.email})

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }
# 🛡️ Protected route — User
@router.get("/me", summary="Get current user info")
def get_profile(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email,
        #"role": current_user.role
        "is_admin": current_user.is_admin  
    }

# 🛡️ Protected route — Admin only
@router.get("/admin/dashboard", summary="Admin only route")
def admin_dashboard(admin_user: User = Depends(require_admin)):
    return {
        "message": f"Welcome admin {admin_user.name}!"
    }

from datetime import datetime, timedelta
import uuid
from app.auth.models import PasswordResetToken
from app.auth.schemas import ForgotPasswordRequest, ResetPasswordRequest

@router.post("/forgot-password", summary="Send password reset token to email")
def forgot_password(payload: ForgotPasswordRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="No user found with this email")

    # Generate token
    token = str(uuid.uuid4())
    expiration = datetime.utcnow() + timedelta(minutes=30)

    reset_token = PasswordResetToken(
        user_id=user.id,
        token=token,
        expiration_time=expiration
    )

    db.add(reset_token)
    db.commit()

    # Simulate email sending
    print(f"🔐 Password reset token for {user.email}: {token}")

    return {"message": "Password reset link sent to your email "}


@router.post("/reset-password", summary="Reset password using token")
def reset_password(payload: ResetPasswordRequest, db: Session = Depends(get_db)):
    token_entry = db.query(PasswordResetToken).filter(
        PasswordResetToken.token == payload.token,
        PasswordResetToken.used == False
    ).first()

    if not token_entry or token_entry.expiration_time < datetime.utcnow():
        raise HTTPException(status_code=400, detail="Invalid or expired token")

    user = db.query(User).filter(User.id == token_entry.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.hashed_password = utils.hash_password(payload.new_password)
    token_entry.used = True  # Mark the token as used

    db.commit()

    return {"message": "Password has been reset successfully"}
