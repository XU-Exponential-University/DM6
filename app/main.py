from fastapi import FastAPI, Request
from app.users import router as user_router
from app.users import get_all_users
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
app = FastAPI()
app.include_router(user_router)

@app.get("/")
def home(request: Request):
    users = get_all_users()
    return templates.TemplateResponse("home.html", {"request": request, "users": users})