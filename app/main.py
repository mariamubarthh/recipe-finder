from fastapi import  FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from .database import get_db
from .routers import recepie,users,auth,admin
from fastapi import FastAPI,Request,Depends
from sqlalchemy.orm import Session
from fastapi.staticfiles import StaticFiles

app = FastAPI()    #create instance of fastapi
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


origins= ["*"]         #all origins are allowed(domains/sites)

app.add_middleware(
    CORSMiddleware,          #a func that runs before every req
    allow_origins=origins,        #which domains can talk to our api
    allow_credentials=True,
    allow_methods=["*"],     #allow specific http methods
    allow_headers=["*"],
)




app.include_router(admin.router)       

app.include_router(users.router)

app.include_router(auth.router)

app.include_router(recepie.router)












#to show main page
@app.get("/main")
async def mainhomepage(request: Request):
   return templates.TemplateResponse("mainhome.html", {"request": request})


#function to upload image
@app.post("/upload")
def upload(file: UploadFile = File(...),db: Session = Depends(get_db)):
    try:
        contents = file.file.read()
        file_loc=f"static/{file.filename}"
        with open( file_loc, "wb") as f:
            f.write(contents)
        global image_path_save    
        image_path_save=f"{file.filename}"
        
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()
        
    return {"message": f"Successfuly uploaded {file.filename}"}







