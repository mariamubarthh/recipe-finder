from pydantic import BaseModel, EmailStr



#Recipe Schemas
class RecepieBase(BaseModel):
    dishname:str
    instructions:str
    ingredients:str
    image_path :str
    
    

class RecepieCreate(RecepieBase):
    pass                       


    
class RecepieOut(BaseModel):
   dishname:str
   instructions:str
   ingredients:str
   
   class Config:
      orm_mode = True  


#Schema for Creating User
class UserCreate(BaseModel):
    email:EmailStr
    password:str 
        
class UserLogin(BaseModel):
    email:EmailStr
    password:str
    

           
           

                   