# -----------------------------------------
# FIXMYCAMPUS - VALIDATION MODULE
# -----------------------------------------


# -----------------------------------------
# CHECK TEXT INPUT
# -----------------------------------------

def validate_text(value, field_name):

    value = value.strip()

    if value == "":
        return False, field_name + " cannot be empty."

    return True, ""


# -----------------------------------------
# CHECK ISSUE ID
# -----------------------------------------

def validate_issue_id(value):

    value = value.strip()

    if value == "":
        return False, "Issue ID cannot be empty."

    try:
        issue_id = int(value)

        if issue_id <= 0:
            return False, "Issue ID must be a positive number."

        return True, issue_id

    except ValueError:

        return False, "Issue ID must be a number."


# -----------------------------------------
# CHECK SEVERITY CHOICE
# -----------------------------------------

def validate_severity_choice(choice):

    choice = choice.strip()

    if choice in ["1", "2", "3"]:
        return True, ""

    return False, "Please select severity 1, 2, or 3."


# -----------------------------------------
# CHECK STATUS CHOICE
# -----------------------------------------

def validate_status_choice(choice):

    choice = choice.strip()

    if choice in ["1", "2", "3"]:
        return True, ""

    return False, "Please select status 1, 2, or 3."


# -----------------------------------------
# CHECK DELETE CONFIRMATION
# -----------------------------------------

def validate_confirmation(value):

    value = value.strip().lower()

    if value == "yes":
        return True

    if value == "no":
        return False

    return None