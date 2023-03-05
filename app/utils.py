from passlib.context import CryptContext
from . import models 

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#convert password into hash 
def hash(password:str):
    return pwd_context.hash(password)


#will decode hash password to verify with input password
def verify(plain_pw, hashed_pw):
    return pwd_context.verify(plain_pw,hashed_pw)

#for authenticating user
def authenticate_user(db, username: str, password: str):
    user = db.query(models.Admin).filter(models.Admin.email== username).first()
    if not user:
        return False
    if not pwd_context.verify(password, user.password):
        return False
    return user