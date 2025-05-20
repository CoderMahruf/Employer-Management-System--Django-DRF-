# Employer Management System API

A simple Django REST Framework API to manage employers with JWT authentication.

---

## 🔥 Features

- Custom user authentication with JWT tokens  
- CRUD operations for Employers  
- Secure endpoints only accessible by authenticated users  
- Users see only their own employers (unless admin)  

---

## 🚀 How to Run Locally

### 1. Clone the Repo

```bash
git clone <https://github.com/CoderMahruf/Employer-Management-System-Django-DRF>
```

### 2. Install Dependencies
```
pip install -r requirements.txt
```

### 3. Run Migrations
```
python manage.py migrate
````
### 4. Create Superuser (Optional, for admin access)
```
python manage.py createsuperuser
```
### 5.  Run the Server
```
python manage.py runserver
```
## ⚡ Tips
- Always add a trailing slash (/) at the end of API URLs

- Use Postman 

- Keep your JWT access token fresh with refresh tokens
- Please open Scrrenshots file and see this.