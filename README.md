# Student Attendance Management System

A Python-based **Student Attendance Management System** developed as a learning project to explore Python, Object-Oriented Programming, software architecture, database integration, and REST APIs.

The project started with **CSV-based data storage** and is currently being upgraded to use **MySQL** through a repository-based architecture.

---

## 📌 Project Overview

The Student Attendance Management System is designed to manage students, teachers, classrooms, and attendance records.

The system is being developed with a layered architecture so that responsibilities are separated between different parts of the application.

The main architectural flow is:

```text
main.py
   ↓
Managers
   ↓
Repositories
   ↓
Database
   ↓
MySQL
```

Each layer has a specific responsibility instead of putting all the logic into one file.

---

## ✨ Features

### Student Management

* Add students
* Remove students
* Search for students
* View students
* Store student details such as:

  * Student ID
  * Student name
  * Date of birth

### Attendance Management

* Record attendance
* Mark students as:

  * Present
  * Absent
  * Holiday
  * Half Day
* View attendance records
* Calculate attendance percentage
* Generate attendance summaries

### Teacher Management

* Manage teachers
* Assign teachers to classrooms
* Support the relationship between teachers and classrooms

### Classroom Management

* Create and manage classrooms
* Associate students with classrooms
* Associate class teachers with classrooms

### Data Persistence

The project initially used **CSV files** for persistent storage.

The project is now being migrated to **MySQL**, with repositories being introduced to handle database operations.

---

## 🏗️ Project Architecture

The project follows a layered approach:

### Models

Models represent the data used by the application.

```text
models/
├── student.py
├── attendance.py
├── teacher.py
└── classroom.py
```

**Models store data.**

For example, the `Student` model represents information about a student.

---

### Managers

Managers contain the application's business logic and make decisions about how operations should be performed.

```text
managers/
├── student_manager.py
├── attendance_manager.py
├── teacher_manager.py
└── classroom_manager.py
```

**Managers make decisions.**

For example, `StudentManager` can check whether a student already exists before allowing a new student to be added.

---

### Repositories

Repositories form the data-access layer between managers and the database.

```text
repositories/
└── student_repository.py
```

**Repositories handle data storage and retrieval.**

They are responsible for operations such as:

* Adding data to the database
* Removing data
* Searching for data
* Retrieving data

The repository layer is currently being implemented as part of the MySQL integration.

---

### Database

`database.py` manages the connection between the Python application and MySQL.

**Database connects to MySQL.**

It is responsible for things such as:

* Establishing a database connection
* Providing access to the database connection
* Closing the connection

---

### Main Program

`main.py` acts as the entry point of the application.

**`main.py` ties everything together.**

It provides the user interface and connects the different parts of the application.

---

## 📂 Current Project Structure

```text
Student-Attendance-Management-System/
│
├── models/
│   ├── __init__.py
│   ├── student.py
│   ├── attendance.py
│   ├── teacher.py
│   └── classroom.py
│
├── managers/
│   ├── __init__.py
│   ├── student_manager.py
│   ├── attendance_manager.py
│   ├── teacher_manager.py
│   └── classroom_manager.py
│
├── repositories/
│   ├── __init__.py
│   └── student_repository.py
│
├── database.py
├── main.py
├── README.md
└── .gitignore
```

The repository layer will expand as the remaining database-related components are implemented.

---

## 🗄️ Database

The project is currently being migrated from CSV persistence to **MySQL**.

The intended database structure will contain tables corresponding to the application's main entities, such as:

```text
Students
Attendance
Teachers
Classrooms
```

The exact database design will evolve as the SQL integration is implemented.

---

## 🔄 Data Flow

For example, when adding a student:

```text
User
 ↓
main.py
 ↓
StudentManager
 ↓
StudentRepository
 ↓
Database
 ↓
MySQL
```

Each layer handles a different responsibility.

For example:

* `main.py` receives the user's action.
* `StudentManager` applies business rules.
* `StudentRepository` performs the required data-storage operation.
* `Database` provides the MySQL connection.
* MySQL stores the actual data.

---

## 🛠️ Technologies Used

* **Python**
* **Object-Oriented Programming**
* **MySQL**
* **Git**
* **GitHub**
* **PyCharm**

### Planned Technologies

* **FastAPI**
* **Alembic**
* REST APIs
* Authentication and authorization

---

## 📈 Development Roadmap

The project is being developed in stages.

### Phase 1 — Console Application

* Student management
* Attendance management
* Add/remove/search/view operations
* Basic attendance reports

### Phase 2 — Multiple Classes / Sections

* Support multiple classrooms
* Associate students with classrooms

### Phase 3 — Multiple Users / Teachers

* Introduce teacher management
* Class teacher relationships

### Phase 4 — Authentication & Roles

* Username/password system
* Role-based access
* Principal and Class Teacher permissions

### Phase 5 — Password Security

* Password encryption/hashing
* Secure authentication

### Phase 6 — Production Backend

* Prepare the application architecture for a backend environment

### Phase 7 — Teacher & Classroom Management

* ClassTeacher relationships
* Classroom relationships
* Student-classroom relationships

### Phase 8A — MySQL Integration

**Current Phase**

* Database connection
* Repository layer
* Student repository
* SQL CRUD operations
* Replace CSV persistence with MySQL persistence
* Connect Managers → Repositories → Database

### Software Engineering Checkpoint

* Repository/DAO concepts
* Database design improvements
* Alembic database migrations

### Phase 9 — REST API Integration

* FastAPI
* REST endpoints
* Connect the existing application architecture to an API

### Phase 10 — Authentication & Authorization

* User authentication
* Role-based permissions
* Secure access to different resources

### Phase 11 — Refactoring & Finalization

* Refactor code
* Improve project structure
* Testing
* Documentation
* README improvements
* Architecture documentation
* Portfolio preparation

---

## 📍 Current Development Status

**Current phase: Phase 8A — MySQL Integration**

### Completed

* Console-based application
* Student management
* Attendance management
* Attendance reports
* Teacher management
* Classroom management
* Student-classroom relationships
* CSV persistence
* Project restructuring
* `models` package
* `managers` package
* `repositories` package
* Database connection setup
* Git/GitHub version control

### In Progress

* Implementing repository methods
* Implementing SQL CRUD operations
* Connecting managers with repositories
* Migrating persistent storage from CSV to MySQL

### Not Yet Implemented

* Complete MySQL CRUD integration
* FastAPI REST API
* Authentication
* Authorization
* Alembic migrations
* Final refactoring and testing

---

## 🎯 Purpose of the Project

This project is not only intended to create an attendance management application.

It is also being used to learn and apply:

* Python
* Object-Oriented Programming
* Data structures
* CRUD operations
* File persistence
* SQL and relational databases
* MySQL
* Repository architecture
* Dependency Injection
* Software architecture
* Database migrations
* REST APIs
* Authentication
* Git and GitHub
* Software engineering practices

The project is intentionally being developed incrementally so that each architectural concept can be understood and implemented rather than simply copied into the application.

---

## 🧠 Architecture Summary

The core responsibility of each layer can be summarized as:

```text
Models
    → Store data

Managers
    → Make decisions

Repositories
    → Handle data storage

Database
    → Connect to MySQL

main.py
    → Ties everything together
```

This separation allows individual parts of the application to be changed without rewriting the entire system.

---

## 🚀 Future Goal

The final goal is to transform the current console-based application into a properly structured backend system with:

```text
Client
   ↓
FastAPI
   ↓
Managers
   ↓
Repositories
   ↓
Database
   ↓
MySQL
```

with authentication, authorization, database migrations, testing, documentation, and a clean software architecture.

---

## 👨‍💻 Project Status

This project is **actively under development**.

The current focus is completing the **MySQL integration and repository layer** before moving to the REST API stage.
