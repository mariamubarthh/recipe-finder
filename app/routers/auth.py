from fastapi import APIRouter, Depends, Form, status, HTTPException, Response
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from ..database import get_db
from ..import models, utils
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from app import main


router=APIRouter(tags=['Authentication'])



# Authenticate Login through user credentials
@router.post("/login/user")
def login(username: str = Form(...), password: str = Form(...),db: Session = Depends(get_db)):
    #returns username and pw(has no email field)
    login= db.query(models.User).filter(models.User.email==username).first()
    print(login)
    
    if not login:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid credentials")
    if not utils.verify(password, login.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid credentials")
    role = login.role
    #check for user type
    if (role == "guest"):
        return RedirectResponse(url=main.app.url_path_for("searchrecipe"), status_code=status.HTTP_303_SEE_OTHER)
        
    if (role == "admin"):
        return RedirectResponse(url=main.app.url_path_for("adminpage"), status_code=status.HTTP_303_SEE_OTHER)
    
 

