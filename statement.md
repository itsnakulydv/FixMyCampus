# Project Statement

## Project Title

FixMyCampus — Campus Issue Reporting & Tracking System

---

## 1. Problem Statement

Students regularly encounter different problems on campus, including maintenance issues, Wi-Fi problems, water leakage, broken furniture, hostel problems, and cleanliness issues.

A structured system is required to record these issues, store their information, assign priority, track their status, and provide useful information about the overall condition of reported campus issues.

FixMyCampus is designed as a command-line Python application that provides these functions through a simple and structured workflow.

---

## 2. Project Scope

The scope of FixMyCampus includes:

- Reporting campus issues
- Storing issue information
- Assigning severity
- Automatically calculating priority
- Viewing reported issues
- Searching issues
- Updating issue status
- Deleting issues
- Generating campus analytics
- Validating user input
- Storing data using SQLite
- Testing important application functionality

The current project is designed as a command-line application.

---

## 3. Target Users

The primary target users are:

### Students

Students can report campus problems and check their status.

### Campus Support Staff

Support staff can use issue information to understand reported problems and their current status.

### Project Evaluators

The application demonstrates practical implementation of Python programming and software development concepts.

---

## 4. High-Level Features

### Issue Reporting

Users can create a new campus issue.

### Issue Management

Users can view, search, update, and delete issues.

### Priority Management

The system automatically maps severity to priority.

### Status Tracking

Issues can be tracked using:

- Open
- In Progress
- Resolved

### Analytics

The system provides statistics about reported campus issues.

### Data Persistence

SQLite is used to permanently store issue information.

### Validation

User inputs are validated before processing.

### Testing

Important application components are tested using a dedicated test module.

---

## 5. Functional Requirements

### FR1 — Report Issue

The system shall allow users to create a new issue.

### FR2 — Store Issue

The system shall store issue information in an SQLite database.

### FR3 — View Issues

The system shall allow users to view all stored issues.

### FR4 — Search Issues

The system shall allow users to search issues by title, location, or category.

### FR5 — Update Status

The system shall allow users to update an issue status.

### FR6 — Delete Issue

The system shall allow users to delete an existing issue after confirmation.

### FR7 — Calculate Priority

The system shall automatically calculate priority based on severity.

### FR8 — Generate Analytics

The system shall calculate issue statistics and category information.

### FR9 — Validate Input

The system shall validate user-provided input.

### FR10 — Run Tests

The project shall provide tests for important application functionality.

---

## 6. Non-Functional Requirements

### Usability

The application should provide a simple menu-driven command-line interface.

### Reliability

The application should validate input and handle invalid values without terminating unexpectedly.

### Maintainability

The application should use separate modules for database operations, models, services, validation, and testing.

### Performance

The system should perform basic issue operations efficiently for normal campus-scale data.

### Data Persistence

Reported issues should remain available after the application is closed and restarted.

### Error Handling

Invalid issue IDs, empty input, invalid menu selections, and invalid status/severity selections should be handled appropriately.

---

## 7. Technology Requirements

The project uses:

- Python
- SQLite
- SQL
- Object-Oriented Programming
- Modular Programming
- Automated Testing
- Git
- GitHub

---

## 8. Expected Outcome

The expected outcome is a functional command-line application that provides a structured way to report and manage campus issues while demonstrating practical Python programming and software development concepts.