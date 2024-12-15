from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from app.database import get_db_connection

templates = Jinja2Templates(directory="templates")
router = APIRouter(prefix="/users", tags=["Users"])

def get_all_users():
    connection = get_db_connection()
    users = []
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM Users")
            users = cursor.fetchall()
        except Exception as e:
            print(f"Error fetching users: {e}")
        finally:
            connection.close()
    return users

def get_user_by_id(user_id):
    connection = get_db_connection()
    user = None
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM Users WHERE id = %s", (user_id,))
            user = cursor.fetchone()
        except Exception as e:
            print(f"Error fetching user: {e}")
        finally:
            connection.close()
    return user

def save_user(username, password, email):
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO Users (username, password, email) VALUES (%s, %s, %s)",
                (username, password, email)
            )
            connection.commit()
        except Exception as e:
            print(f"Error saving user: {e}")
        finally:
            connection.close()

def update_user(user_id, username, email, password):
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(
                "UPDATE Users SET username = %s, email = %s, password = %s WHERE id = %s",
                (username, email, password, user_id)
            )
            connection.commit()
        except Exception as e:
            print(f"Error updating user: {e}")
        finally:
            connection.close()

def delete_user_by_id(user_id):
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM Users WHERE id = %s", (user_id,))
            connection.commit()
        except Exception as e:
            print(f"Error deleting user: {e}")
        finally:
            connection.close()

# Route: http://localhost:5000/users/ (GET)
@router.get("/")
def list_users(request: Request):
    users = get_all_users()  # Fetch all users using the method in users.py
    return templates.TemplateResponse("list_users.html", {"request": request, "users": users})

# Route: http://localhost:5000/users/create (GET)
@router.get("/create")
def create_user_form(request: Request):
    return templates.TemplateResponse("create_user.html", {"request": request})

# Route: http://localhost:5000/users/create (POST)
@router.post("/create")
def create_user(username: str = Form(...), password: str = Form(...), email: str = Form(...)):
    save_user(username, password, email)
    return RedirectResponse("/users/", status_code=303)


@router.get("/edit/{user_id}")
def edit_user_form(request: Request, user_id: int):
    user = get_user_by_id(user_id)
    if not user:
        return RedirectResponse("/users", status_code=404)
    return templates.TemplateResponse("edit_user.html", {"request": request, "user": user})

# Route: Process edit form (POST)
@router.post("/edit/{user_id}")
def edit_user(user_id: int, username: str = Form(...), email: str = Form(...), password: str = Form(...)):
    update_user(user_id, username, email, password)
    return RedirectResponse("/users", status_code=303)

@router.get("/delete/{user_id}")
def delete_user(user_id: int):
    delete_user_by_id(user_id)
    return RedirectResponse("/users", status_code=303)