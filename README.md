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

## Styling
- Bootstrap: Provides responsive design and pre-built components and added to the `base.html` file
- Google Fonts: Used to improve typography and added `Rubik` https://fonts.google.com/specimen/Rubik font to the `base.html` file 
- Font Awesome: Adds icons for better visual representation. Please add your own kit in `base.html` file

## Setup Instructions
1. **Clone Repository:** Open a terminal/CMD and execute: `git clone git@github.com:XU-Exponential-University/DM6.git`
2. **Open the Project:** Open your project in `Intellij IDEA`
3. **Set Up a Virtual Environment:** 
```python
python3 -m venv myenv # On Windows: python -m venv myenv
source myenv/bin/activate   # On Windows: myenv\Scripts\activate
```
4. **Install Dependencies:**
```python
pip install -r requirements.txt
```
5. **Set Up the Database:**
  - Open Docker Desktop
  - Go to the `Images` tab 
    > If it’s not present, pull the image (`mysql`) from the search box
  - Locate the MySQL image (e.g., `mysql:8.0`) and click on it
  - Click the `Run` button
  - Expand `Optional settings`
  - Add a Container Name e.g. `MyServer`
  - Set a port number e.g. `3310`
  - and set an Environment Variable: `MYSQL_ROOT_PASSWORD` and the value `secret`
  - Click `Run`
6. **Add MySQL as a Data Source:**
  - On Intellij, Go to `View > Tool Windows > Database`.
  - Click the `+` icon in the Database window.
    - Select `Data Source > MySQL`.
      - Configure Connection Details:
        - Add a name e.g.: `MyUserServer`
        - Host: `localhost` 
        - Port: `3310` 
        - User: `root` 
        - Password: `secret`
        - IntelliJ may prompt you to download the MySQL JDBC Driver. Allow it to download.
        - Click `Test Connection` to verify the setup.
        - If successful, Click OK to save the data source.
        - Expand the connected MySQL data source in the Database tab and click on `...` and select `All Schemes`
        - Right click on `MyUserServer` and select `New > Query Console`
        - Run the following in the `console`
          ```mysql
          CREATE DATABASE user_management;
          USE user_management;
        
          CREATE TABLE Users (
          id INT AUTO_INCREMENT PRIMARY KEY,
          username VARCHAR(22) NOT NULL,
          email VARCHAR(50) NOT NULL UNIQUE,
          password VARCHAR(30) NOT NULL
          );
          ```
7. 