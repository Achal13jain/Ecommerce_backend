from passlib.context import CryptContext #Import password hashing framework

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:#Hashing a plain password
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:#Compare entered password with the stored hash
    return pwd_context.verify(plain_password, hashed_password)
