### README.md for Django Student Management System

# Django Student Management System Capstone Final Project Submission.

This is a Student Management System developed by Binyam Tesfaye using Python (Django),HTML, and CSS. 

## Distinctiveness and Complexity

### Distinctiveness
This project is distinct from other projects in the course due to its focus on managing academic activities within an educational institution. Unlike social networks or e-commerce sites, this system is designed to handle administrative tasks, track student performance, manage staff, and streamline communication within an educational context. The system supports multiple user roles, each with specific permissions and features, making it a versatile tool for educational administration.

### Complexity
The complexity of this project lies in its comprehensive functionality and use of multiple user roles (Admin, Staff, and Students), each with specific permissions and features. The project incorporates various Django models to manage entities such as Students, Staff, Courses, and Subjects. Additionally, it involves complex data relationships and includes both server-side and client-side validations. The use of JavaScript enhances interactivity, particularly in dynamically updating attendance records and displaying performance charts.

## Features

### Admin Users Can
1. See overall summary charts of students' performance, staff performances, courses, subjects, leave, etc.
2. Manage Staff (Add, Update, and Delete)
3. Manage Students (Add, Update, and Delete)
4. Manage Courses (Add, Update, and Delete)
5. Manage Subjects (Add, Update, and Delete)
6. Manage Sessions (Add, Update, and Delete)
7. View Student Attendance
8. Review and Reply to Student/Staff Feedback
9. Review (Approve/Reject) Student/Staff Leave

### Staff/Teachers Can
1. See overall summary charts related to their students, their subjects, leave status, etc.
2. Take/Update Students' Attendance
3. Add/Update Results
4. Apply for Leave
5. Send Feedback to HOD

### Students Can
1. See overall summary charts related to their attendance, their subjects, leave status, etc.
2. View Attendance
3. View Results
4. Apply for Leave
5. Send Feedback to HOD

## How to Install and Run this Project

### Pre-Requisites
1. Install Python Latest Version
   - [Python Downloads](https://www.python.org/downloads/)
2. Install Pip (Package Manager)
   - [Pip Installation](https://pip.pypa.io/en/stable/installing/)
   - *Alternative to Pip is Homebrew*

### Installation Steps

**1. Enter the Project Directory**
```
$ cd django-student-management-system
```

**2. Install Requirements from `requirements.txt`**
```bash
$ pip install -r requirements.txt
```

**3. Add the Hosts**
- Go to `settings.py` file.
- On allowed hosts, add `['*']`.
```python
ALLOWED_HOSTS = ['*']
```
*No need to change on Mac.*

**4. Run the Server**

Command for PC:
```bash
$ python manage.py runserver
```

Command for Mac:
```bash
$ python3 manage.py runserver
```

**5. Login Credentials**

Create Super User (HOD)
```
$ python manage.py createsuperuser
```
Then add Email, Username, and Password.

**Or Use Default Credentials**

*For HOD / SuperAdmin*
- Email: admin1@gmail.com
- Password: 1234

*For Staff*
- Email: teacher1@gmail.com
- Password: 1234

*For Student*
- Email: student12@gmail.com
- Password: 1234

## File Structure

### Project Root
- `.DS_Store`: System file.
- `db.sqlite3`: The SQLite database file.
- `manage.py`: Django's command-line utility for administrative tasks.
- `README.md`: Project documentation file.
- `requirements.txt`: List of Python packages required to run the project.

### Directories
- `media/`: Directory to store media files uploaded by users.
- `static/`: Directory to store static files (CSS, JavaScript, images).
- `student_management_app/`: Main application directory.
  - `.DS_Store`: System file.
  - `admin.py`: Admin configuration.
  - `apps.py`: Application configuration.
  - `EmailBackEnd.py`: Custom email backend for authentication.
  - `forms.py`: Forms used in the application.
  - `HodViews.py`: Views for HOD (Admin) functionalities.
  - `LoginCheckMiddleWare.py`: Middleware for login check.
  - `models.py`: Database models.
  - `StaffViews.py`: Views for Staff functionalities.
  - `StudentViews.py`: Views for Student functionalities.
  - `templates/`: Directory containing HTML templates.
  - `tests.py`: Test cases.
  - `urls.py`: URL routing configuration.
  - `views.py`: General views.
  - `__init__.py`: Package initialization file.
  - `__pycache__/`: Directory for compiled Python files.

- `student_management_system/`: Project configuration directory.
  - `asgi.py`: ASGI configuration.
  - `settings.py`: Project settings.
  - `urls.py`: URL routing configuration.
  - `wsgi.py`: WSGI configuration.
  - `__init__.py`: Package initialization file.
  - `__pycache__/`: Directory for compiled Python files.

## Additional Information
The project leverages Django's robust framework to manage complex relationships and ensure data integrity. The integration of JavaScript enhances user experience by providing real-time updates and feedback.

### Requirements
Ensure you have the following packages installed (as listed in `requirements.txt`):
- Django
- [Any other packages you used]

This Student Management System is a comprehensive tool designed to facilitate administrative and academic processes within an educational institution. It highlights the practical application of Django and JavaScript in building dynamic web applications.