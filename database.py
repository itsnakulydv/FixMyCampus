import sqlite3


# -----------------------------------------
# DATABASE CONFIGURATION
# -----------------------------------------

DATABASE_NAME = "fixmycampus.db"


# -----------------------------------------
# CONNECT TO DATABASE
# -----------------------------------------

def connect_database():

    return sqlite3.connect(DATABASE_NAME)


# -----------------------------------------
# CREATE TABLE
# -----------------------------------------

def create_table():

    connection = connect_database()

    cursor = connection.cursor()


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS issues (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            title TEXT NOT NULL,

            location TEXT NOT NULL,

            category TEXT NOT NULL,

            description TEXT NOT NULL,

            severity TEXT NOT NULL,

            priority TEXT NOT NULL,

            status TEXT NOT NULL

        )
    """)


    connection.commit()

    connection.close()


# -----------------------------------------
# ADD ISSUE
# -----------------------------------------

def add_issue(issue):

    connection = connect_database()

    cursor = connection.cursor()


    cursor.execute("""
        INSERT INTO issues
        (
            title,
            location,
            category,
            description,
            severity,
            priority,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (

        issue["title"],
        issue["location"],
        issue["category"],
        issue["description"],
        issue["severity"],
        issue["priority"],
        issue["status"]

    ))


    connection.commit()


    issue_id = cursor.lastrowid


    connection.close()


    return issue_id


# -----------------------------------------
# GET ALL ISSUES
# -----------------------------------------

def get_all_issues():

    connection = connect_database()

    cursor = connection.cursor()


    cursor.execute("""
        SELECT
            id,
            title,
            location,
            category,
            description,
            severity,
            priority,
            status
        FROM issues
        ORDER BY id
    """)


    rows = cursor.fetchall()


    connection.close()


    issues = []


    for row in rows:

        issue = {

            "id": row[0],

            "title": row[1],

            "location": row[2],

            "category": row[3],

            "description": row[4],

            "severity": row[5],

            "priority": row[6],

            "status": row[7]

        }


        issues.append(issue)


    return issues


# -----------------------------------------
# SEARCH ISSUES
# -----------------------------------------

def search_issues(search):

    connection = connect_database()

    cursor = connection.cursor()


    search_value = "%" + search + "%"


    cursor.execute("""
        SELECT
            id,
            title,
            location,
            category,
            description,
            severity,
            priority,
            status
        FROM issues
        WHERE LOWER(title) LIKE LOWER(?)
           OR LOWER(location) LIKE LOWER(?)
           OR LOWER(category) LIKE LOWER(?)
        ORDER BY id
    """, (
        search_value,
        search_value,
        search_value
    ))


    rows = cursor.fetchall()


    connection.close()


    issues = []


    for row in rows:

        issue = {

            "id": row[0],

            "title": row[1],

            "location": row[2],

            "category": row[3],

            "description": row[4],

            "severity": row[5],

            "priority": row[6],

            "status": row[7]

        }


        issues.append(issue)


    return issues


# -----------------------------------------
# UPDATE ISSUE STATUS
# -----------------------------------------

def update_status(issue_id, status):

    connection = connect_database()

    cursor = connection.cursor()


    cursor.execute("""
        UPDATE issues

        SET status = ?

        WHERE id = ?
    """, (
        status,
        issue_id
    ))


    connection.commit()


    updated = cursor.rowcount


    connection.close()


    return updated


# -----------------------------------------
# DELETE ISSUE
# -----------------------------------------

def delete_issue(issue_id):

    connection = connect_database()

    cursor = connection.cursor()


    cursor.execute("""
        DELETE FROM issues

        WHERE id = ?
    """, (
        issue_id,
    ))


    connection.commit()


    deleted = cursor.rowcount


    connection.close()


    return deleted


# -----------------------------------------
# GET ISSUE BY ID
# -----------------------------------------

def get_issue_by_id(issue_id):

    connection = connect_database()

    cursor = connection.cursor()


    cursor.execute("""
        SELECT
            id,
            title,
            location,
            category,
            description,
            severity,
            priority,
            status
        FROM issues

        WHERE id = ?
    """, (
        issue_id,
    ))


    row = cursor.fetchone()


    connection.close()


    if row is None:

        return None


    issue = {

        "id": row[0],

        "title": row[1],

        "location": row[2],

        "category": row[3],

        "description": row[4],

        "severity": row[5],

        "priority": row[6],

        "status": row[7]

    }


    return issue