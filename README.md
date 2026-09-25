# FixMyCampus

## Campus Issue Reporting & Tracking System

FixMyCampus is a Python-based command-line application designed to help students report, track, search, update, and manage common campus issues.

The system stores issue information using SQLite and provides automatic priority calculation and campus analytics.

---

## Problem

Students may face different problems on campus such as:

- Broken fans
- Wi-Fi problems
- Water leakage
- Classroom maintenance issues
- Broken furniture
- Hostel problems
- Cleanliness issues

Without a structured system, reporting and tracking these problems can become difficult.

FixMyCampus provides a simple digital system for recording and managing these issues.

---

## Objectives

The main objectives of FixMyCampus are:

1. Allow students to report campus issues.
2. Store issue information permanently.
3. Automatically calculate issue priority.
4. Allow users to search issues.
5. Track issue status.
6. Delete incorrect or unnecessary reports.
7. Provide campus issue analytics.
8. Demonstrate Python programming, OOP, modular programming, validation, database handling, and testing.

---

## Features

### 1. Report an Issue

Users can report an issue by entering:

- Issue title
- Location
- Category
- Description
- Severity

The system automatically assigns priority.

### 2. Automatic Priority

Priority is calculated from severity:

| Severity | Priority |
|----------|----------|
| Low | Normal |
| Medium | Important |
| High | Urgent |

### 3. View Issues

Users can view all reported campus issues.

### 4. Search Issues

Users can search issues using:

- Title
- Location
- Category

### 5. Update Status

An issue can have one of three statuses:

- Open
- In Progress
- Resolved

### 6. Delete Issue

Users can delete an existing issue after confirmation.

### 7. Campus Analytics

The system calculates:

- Total issues
- Open issues
- In-progress issues
- Resolved issues
- Urgent issues
- Resolution rate
- Most common category
- Category-wise issue count

### 8. SQLite Database

Issue information is stored permanently using SQLite.

### 9. Input Validation

The system validates:

- Empty text
- Issue IDs
- Severity choices
- Status choices
- Delete confirmation

### 10. Testing

The project contains automated tests for important project functionality.

---

## Technologies Used

- Python
- SQLite
- SQL
- Object-Oriented Programming
- Modular Programming
- File Handling
- Input Validation
- Automated Testing
- Git & GitHub

---

## Project Structure

```text
FixMyCampus/
│
├── main.py
│
├── database/
│   └── database.py
│
├── models/
│   └── issue.py
│
├── services/
│   ├── priority_engine.py
│   └── analytics.py
│
├── utils/
│   └── validation.py
│
├── tests/
│   └── test_project.py
│
├── README.md
├── statement.md
├── requirements.txt
└── .gitignore