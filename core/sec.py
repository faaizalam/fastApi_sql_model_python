from passlib.context import CryptContext

pwd_context=CryptContext(schemes=["bcrypt"],DeprecationWarning="auto")




def get_password_hash(password:str) -> str:
    return pwd_context.hash(password)


def veirfy_password(plain_password:str,hashed_pass:str)->bool:
    return pwd_context.verify(plain_password,hashed_pass)