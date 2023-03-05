from fastapi import HTTPException,status,Depends,APIRouter,Form,Request
from .. import models
from sqlalchemy.orm import Session
from ..database import  get_db
from sqlalchemy import func
from .. import main
from fastapi.responses import RedirectResponse,HTMLResponse



router=APIRouter(prefix="/recipe",
                 tags=['Recepies'])   #bcz every url has prefix  so we have initially defined it



#route for create recipe page
@router.get("/addnew")
async def addnew(request: Request):
   return main.templates.TemplateResponse("addnew.html", {"request": request})

#route for search recipe page
@router.get("/searchrecipe")
async def searchrecipe(request: Request):
   return main.templates.TemplateResponse("searchrecipe.html", {"request": request})


 
 
 #to get recipes matched with searched keyword
@router.get("/search")
async def search_results(request: Request,searched_item:str, db: Session = Depends(get_db)):
    # query the database for recipes matching the search term
    recipes = db.query(models.Recepie).filter(models.Recepie.dishname.ilike(f"%{searched_item}%")).all()
    # render the search results template with the matching recipes
    return main.templates.TemplateResponse("searched_recipes_results.html", {"request": request, "recipes": recipes})




#to fetch all recipes 
@router.get("/all", response_class=HTMLResponse)
async def read_recipes(request: Request, db: Session = Depends(get_db)):
    recipes = db.query(models.Recepie).all()
    return main.templates.TemplateResponse("searched_recipes_results.html", {"request": request, "recipes": recipes})



# to get details of a recipe based on its dishname
@router.get("/{dishname}")
async def search_results(request: Request,dishname:str, db: Session = Depends(get_db)):
    # query the database for recipes matching the search term
    recipes = db.query(models.Recepie).filter(models.Recepie.dishname.contains(dishname)).first()
    
    if recipes is None:
        # return a 404 response if the recipe is not found
        raise HTTPException(status_code=404, detail="Recipe not found")
    
    # render the search results template with the matching recipes
    if recipes.instructions:
        # split the instructions into lines and strip whitespace from each line
        instructions = [line.strip() for line in recipes.instructions.split('\n')]
    else:
        # set the instructions to an empty list if the field is empty
        instructions = []
    return main.templates.TemplateResponse("one_recipe.html", {"request": request, "recipes": recipes,"instructions":instructions})



# route for adding new  recipe
@router.post("/add", status_code=status.HTTP_201_CREATED)
async def add_new_recepie(request: Request, name: str = Form(...),ingredients: str = Form(...),instruction: str = Form(...), db: Session = Depends(get_db) ):               #extracting body from users data and savingit in post 
    new_rec=models.Recepie(dishname = name,ingredients=ingredients,instructions=instruction,image_path = main.image_path_save)  #unpacking all the fields same like we do individually(title=post.title etc)
    db.add(new_rec)
    db.commit()
    db.refresh(new_rec)      #retrieving the new post and storing back into new_post
    return RedirectResponse(url=main.app.url_path_for("adminpage"), status_code=status.HTTP_303_SEE_OTHER)
 










