# =========================================
# FIXMYCAMPUS
# Campus Issue Reporting & Tracking System
# =========================================


# -----------------------------------------
# IMPORTS
# -----------------------------------------

from database.database import (
    create_table,
    add_issue,
    get_all_issues,
    get_issue_by_id,
    update_status,
    delete_issue,
    search_issues
)

from models.issue import Issue

from services.priority_engine import (
    calculate_priority,
    get_severity
)

from services.analytics import (
    calculate_analytics,
    display_analytics
)

from utils.validation import (
    validate_text,
    validate_issue_id,
    validate_severity_choice,
    validate_status_choice,
    validate_confirmation
)


# -----------------------------------------
# CREATE DATABASE TABLE
# -----------------------------------------

create_table()


# -----------------------------------------
# DISPLAY MAIN MENU
# -----------------------------------------

def show_menu():

    print("\n" + "=" * 55)
    print("                    FIXMYCAMPUS")
    print("           Campus Issue Reporting System")
    print("=" * 55)

    print("1. Report an Issue")
    print("2. View All Issues")
    print("3. Search Issue")
    print("4. Update Issue Status")
    print("5. Delete Issue")
    print("6. Campus Analytics")
    print("7. Exit")

    print("=" * 55)


# -----------------------------------------
# GET TEXT INPUT
# -----------------------------------------

def get_text_input(field_name):

    while True:

        value = input(
            f"Enter {field_name}: "
        ).strip()

        valid, message = validate_text(
            value,
            field_name
        )

        if valid:
            return value

        print(message)


# -----------------------------------------
# REPORT NEW ISSUE
# -----------------------------------------

def report_issue():

    print("\n" + "-" * 55)
    print("                  REPORT AN ISSUE")
    print("-" * 55)


    # -----------------------------------------
    # GET ISSUE DETAILS
    # -----------------------------------------

    title = get_text_input("issue title")

    location = get_text_input("location")

    category = get_text_input("category")

    description = get_text_input("description")


    # -----------------------------------------
    # SELECT SEVERITY
    # -----------------------------------------

    print("\nSelect severity:")

    print("1. Low")
    print("2. Medium")
    print("3. High")


    while True:

        severity_choice = input(
            "Enter severity: "
        ).strip()


        valid, message = validate_severity_choice(
            severity_choice
        )


        if valid:
            break


        print(message)


    severity = get_severity(
        severity_choice
    )


    # -----------------------------------------
    # CALCULATE PRIORITY
    # -----------------------------------------

    priority = calculate_priority(
        severity
    )


    # -----------------------------------------
    # CREATE ISSUE OBJECT
    # -----------------------------------------

    issue = Issue(

        title=title,

        location=location,

        category=category,

        description=description,

        severity=severity,

        priority=priority,

        status="Open"

    )


    # -----------------------------------------
    # SAVE TO DATABASE
    # -----------------------------------------

    issue_id = add_issue(
        issue.to_dict()
    )


    # -----------------------------------------
    # DISPLAY SUCCESS
    # -----------------------------------------

    print("\n" + "=" * 55)

    print("           ISSUE REPORTED SUCCESSFULLY")

    print("=" * 55)

    print("Issue ID :", issue_id)

    print("Title    :", title)

    print("Location :", location)

    print("Category :", category)

    print("Severity :", severity)

    print("Priority :", priority)

    print("Status   : Open")

    print("=" * 55)


# -----------------------------------------
# DISPLAY SINGLE ISSUE
# -----------------------------------------

def display_issue(issue):

    print("\n" + "-" * 55)

    print("Issue ID    :", issue["id"])

    print("Title       :", issue["title"])

    print("Location    :", issue["location"])

    print("Category    :", issue["category"])

    print("Description :", issue["description"])

    print("Severity    :", issue["severity"])

    print("Priority    :", issue["priority"])

    print("Status      :", issue["status"])

    print("-" * 55)


# -----------------------------------------
# VIEW ALL ISSUES
# -----------------------------------------

def view_issues():

    print("\n" + "-" * 55)
    print("                    ALL ISSUES")
    print("-" * 55)


    issues = get_all_issues()


    if len(issues) == 0:

        print("No issues have been reported yet.")

        return


    for issue in issues:

        display_issue(issue)


    print("\n" + "-" * 55)

    print("Total Issues:", len(issues))


# -----------------------------------------
# SEARCH ISSUE
# -----------------------------------------

def search_issue():

    print("\n" + "-" * 55)
    print("                    SEARCH ISSUE")
    print("-" * 55)


    search_value = get_text_input(
        "issue title, location, or category"
    )


    results = search_issues(
        search_value
    )


    if len(results) == 0:

        print("\nNo matching issue found.")

        return


    print("\nMatching Issues:")


    for issue in results:

        display_issue(issue)


    print("\n" + "-" * 55)

    print(
        "Results Found:",
        len(results)
    )


# -----------------------------------------
# UPDATE ISSUE STATUS
# -----------------------------------------

def update_issue_status():

    print("\n" + "-" * 55)
    print("               UPDATE ISSUE STATUS")
    print("-" * 55)


    # -----------------------------------------
    # GET ISSUE ID
    # -----------------------------------------

    while True:

        value = input(
            "Enter Issue ID: "
        ).strip()


        valid, result = validate_issue_id(
            value
        )


        if valid:

            issue_id = result

            break


        print(result)


    # -----------------------------------------
    # FIND ISSUE
    # -----------------------------------------

    issue = get_issue_by_id(
        issue_id
    )


    if issue is None:

        print("Issue not found.")

        return


    print("\nCurrent Status:")

    print(issue["status"])


    # -----------------------------------------
    # SELECT NEW STATUS
    # -----------------------------------------

    print("\nSelect new status:")

    print("1. Open")
    print("2. In Progress")
    print("3. Resolved")


    while True:

        status_choice = input(
            "Enter choice: "
        ).strip()


        valid, message = validate_status_choice(
            status_choice
        )


        if valid:

            break


        print(message)


    if status_choice == "1":

        new_status = "Open"

    elif status_choice == "2":

        new_status = "In Progress"

    else:

        new_status = "Resolved"


    # -----------------------------------------
    # UPDATE DATABASE
    # -----------------------------------------

    result = update_status(
        issue_id,
        new_status
    )


    if result == 0:

        print("Unable to update issue.")

    else:

        print("\nIssue status updated successfully!")

        print("Issue ID   :", issue_id)

        print("New Status :", new_status)


# -----------------------------------------
# DELETE ISSUE
# -----------------------------------------

def delete_issue_menu():

    print("\n" + "-" * 55)
    print("                    DELETE ISSUE")
    print("-" * 55)


    # -----------------------------------------
    # GET ISSUE ID
    # -----------------------------------------

    while True:

        value = input(
            "Enter Issue ID: "
        ).strip()


        valid, result = validate_issue_id(
            value
        )


        if valid:

            issue_id = result

            break


        print(result)


    # -----------------------------------------
    # FIND ISSUE
    # -----------------------------------------

    issue = get_issue_by_id(
        issue_id
    )


    if issue is None:

        print("Issue not found.")

        return


    print("\nIssue selected:")

    display_issue(issue)


    # -----------------------------------------
    # CONFIRM DELETE
    # -----------------------------------------

    while True:

        confirmation = input(
            "\nAre you sure you want to delete "
            "this issue? (yes/no): "
        ).strip().lower()


        result = validate_confirmation(
            confirmation
        )


        if result is True:

            break


        elif result is False:

            print("Deletion cancelled.")

            return


        else:

            print(
                "Please enter yes or no."
            )


    # -----------------------------------------
    # DELETE FROM DATABASE
    # -----------------------------------------

    deleted = delete_issue(
        issue_id
    )


    if deleted == 0:

        print("Unable to delete issue.")

    else:

        print(
            "\nIssue deleted successfully!"
        )


# -----------------------------------------
# CAMPUS ANALYTICS
# -----------------------------------------

def show_campus_analytics():

    issues = get_all_issues()


    analytics = calculate_analytics(
        issues
    )


    display_analytics(
        analytics
    )


# -----------------------------------------
# MAIN PROGRAM
# -----------------------------------------

def main():

    while True:

        show_menu()


        choice = input(
            "Enter your choice: "
        ).strip()


        if choice == "1":

            report_issue()


        elif choice == "2":

            view_issues()


        elif choice == "3":

            search_issue()


        elif choice == "4":

            update_issue_status()


        elif choice == "5":

            delete_issue_menu()


        elif choice == "6":

            show_campus_analytics()


        elif choice == "7":

            print("\n" + "=" * 55)

            print(
                "       Thank you for using FixMyCampus!"
            )

            print("=" * 55)

            break


        else:

            print(
                "\nInvalid choice. "
                "Please select a number from 1 to 7."
            )


# -----------------------------------------
# START APPLICATION
# -----------------------------------------

if __name__ == "__main__":

    main()