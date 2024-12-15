# DM6
## User Management System
A web-based application built with FastAPI to manage users. The system supports the following operations:
- List all users.
  - Accessiable via:
    - Public: `http://localhost:5000/`
    - Admin: `http://localhost:5000/users/`
- Create a new user.
  - Accessible via: `http://localhost:5000/users/creat`
- Edit an existing user.
  - Accessible via: `http://localhost:5000/users/edit/{user_id}`
- Delete a user.
  - Accessible via: `http://localhost:5000/users/delete/{user_id}`

## Folder Structure
```
.
├── app
│   ├── __init__.py
│   ├── database.py         # Database connection setup
│   ├── main.py             # Application entry point
│   └── users.py            # User routes and logic
├── templates
│   ├── base.html           # Base layout for templates
│   ├── create_user.html    # Form to create a new user
│   ├── edit_user.html      # Form to edit user details
│   ├── home.html           # Public user list
│   └── list_users.html     # Admin user list
├── requirements.txt        # Python dependencies
```