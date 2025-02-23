import bcrypt



def hash_password(
    password: str
) -> bytes:
    return bcrypt.hashpw(password.encode(), salt=bcrypt.gensalt())

def validate_password(
    password: str,
    hashed: bytes
) -> bool:
    return bcrypt.checkpw(password=password.encode(), hashed_password=hashed)

