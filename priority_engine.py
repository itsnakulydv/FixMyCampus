# -----------------------------------------
# FIXMYCAMPUS - PRIORITY ENGINE
# -----------------------------------------


# -----------------------------------------
# CALCULATE PRIORITY
# -----------------------------------------

def calculate_priority(severity):

    severity = severity.strip().lower()

    if severity == "high":
        return "Urgent"

    elif severity == "medium":
        return "Important"

    elif severity == "low":
        return "Normal"

    else:
        return "Unknown"


# -----------------------------------------
# GET SEVERITY FROM USER CHOICE
# -----------------------------------------

def get_severity(choice):

    choice = choice.strip()

    if choice == "1":
        return "Low"

    elif choice == "2":
        return "Medium"

    elif choice == "3":
        return "High"

    else:
        return None


# -----------------------------------------
# CHECK VALID SEVERITY
# -----------------------------------------

def is_valid_severity(severity):

    severity = severity.strip().lower()

    if severity == "low":
        return True

    elif severity == "medium":
        return True

    elif severity == "high":
        return True

    return False