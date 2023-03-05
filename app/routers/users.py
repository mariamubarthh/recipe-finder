
from fastapi import Body, Form, Request,Response,HTTPException,status,Depends,APIRouter, FastAPI
from pydantic import EmailStr

from app import main
from .. import models, schemas, utils
from sqlalchemy.orm import Session
from ..database import  get_db
from fastapi.responses import RedirectResponse

router=APIRouter(prefix="/user",
                 tags=['Users'])


#users operations
@router.get("/signup")
async def signup(request: Request):
   return main.templates.TemplateResponse("signup.html", {"request": request})


@router.get("/loginpage")
async def loginpage(request: Request):
    return main.templates.TemplateResponse("loginpage.html", {"request": request})



  
#method to create new user
@router.post("/new", status_code=status.HTTP_201_CREATED)
async def create_users(request:Request,Email:EmailStr= Form(...),pw:str= Form(...), db: Session = Depends(get_db) ):
    
    #hash the pw
    hash_pw=utils.hash(pw)
    pw=hash_pw
    new_user=models.User(email=Email,password=pw,role="guest")  
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return RedirectResponse(url=main.app.url_path_for("searchrecipe"), status_code=status.HTTP_303_SEE_OTHER)



