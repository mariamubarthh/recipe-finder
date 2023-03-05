
from fastapi import Body, Request,Response,HTTPException,status,Depends,APIRouter, FastAPI
from .. import models, schemas, utils
from sqlalchemy.orm import Session
from ..database import  get_db
from .. import main

router = APIRouter(prefix="/admin",
                 tags=['Admin'])




@router.get("/home")
async def adminpage(request: Request):
    return main.templates.TemplateResponse("index.html", {"request": request})