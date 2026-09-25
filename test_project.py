# -----------------------------------------
# FIXMYCAMPUS - PROJECT TESTS
# -----------------------------------------

import sys
import os

# Allow Python to find project modules
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

sys.path.insert(0, PROJECT_ROOT)


# -----------------------------------------
# IMPORT PROJECT MODULES
# -----------------------------------------

from services.priority_engine import (
    calculate_priority,
    get_severity,
    is_valid_severity
)

from services.analytics import calculate_analytics

from utils.validation import (
    validate_text,
    validate_issue_id,
    validate_severity_choice,
    validate_status_choice,
    validate_confirmation
)

from models.issue import Issue


# -----------------------------------------
# PRIORITY TESTS
# -----------------------------------------

def test_priority_low():

    assert calculate_priority("Low") == "Normal"


def test_priority_medium():

    assert calculate_priority("Medium") == "Important"


def test_priority_high():

    assert calculate_priority("High") == "Urgent"


def test_invalid_priority():

    assert calculate_priority("Unknown") == "Unknown"


# -----------------------------------------
# SEVERITY TESTS
# -----------------------------------------

def test_severity_choice():

    assert get_severity("1") == "Low"

    assert get_severity("2") == "Medium"

    assert get_severity("3") == "High"


def test_invalid_severity_choice():

    assert get_severity("5") is None


def test_valid_severity():

    assert is_valid_severity("Low") is True

    assert is_valid_severity("Medium") is True

    assert is_valid_severity("High") is True


def test_invalid_severity():

    assert is_valid_severity("Extreme") is False


# -----------------------------------------
# VALIDATION TESTS
# -----------------------------------------

def test_text_validation():

    valid, message = validate_text(
        "Broken Fan",
        "Title"
    )

    assert valid is True


def test_empty_text_validation():

    valid, message = validate_text(
        "",
        "Title"
    )

    assert valid is False


def test_issue_id_validation():

    valid, result = validate_issue_id("10")

    assert valid is True

    assert result == 10


def test_invalid_issue_id():

    valid, result = validate_issue_id("abc")

    assert valid is False


def test_negative_issue_id():

    valid, result = validate_issue_id("-5")

    assert valid is False


def test_severity_validation():

    assert validate_severity_choice("1")[0] is True

    assert validate_severity_choice("2")[0] is True

    assert validate_severity_choice("3")[0] is True


def test_invalid_severity_validation():

    assert validate_severity_choice("5")[0] is False


def test_status_validation():

    assert validate_status_choice("1")[0] is True

    assert validate_status_choice("2")[0] is True

    assert validate_status_choice("3")[0] is True


def test_invalid_status_validation():

    assert validate_status_choice("5")[0] is False


def test_confirmation():

    assert validate_confirmation("yes") is True

    assert validate_confirmation("no") is False

    assert validate_confirmation("maybe") is None


# -----------------------------------------
# ISSUE MODEL TESTS
# -----------------------------------------

def test_issue_creation():

    issue = Issue(
        title="Broken Fan",
        location="Hostel Block B",
        category="Maintenance",
        description="Fan is not working",
        severity="High",
        priority="Urgent"
    )

    assert issue.title == "Broken Fan"

    assert issue.location == "Hostel Block B"

    assert issue.severity == "High"

    assert issue.priority == "Urgent"

    assert issue.status == "Open"


def test_issue_to_dict():

    issue = Issue(
        title="WiFi Problem",
        location="Library",
        category="Network",
        description="WiFi is slow",
        severity="Medium",
        priority="Important"
    )

    data = issue.to_dict()

    assert data["title"] == "WiFi Problem"

    assert data["category"] == "Network"

    assert data["priority"] == "Important"


def test_issue_from_dict():

    data = {
        "id": 1,
        "title": "Broken Chair",
        "location": "Classroom A",
        "category": "Furniture",
        "description": "Chair is broken",
        "severity": "Low",
        "priority": "Normal",
        "status": "Open"
    }

    issue = Issue.from_dict(data)

    assert issue.id == 1

    assert issue.title == "Broken Chair"

    assert issue.status == "Open"


def test_issue_status_update():

    issue = Issue(
        title="Water Leakage",
        location="Hostel",
        category="Plumbing",
        description="Water leaking",
        severity="High",
        priority="Urgent"
    )

    issue.update_status("Resolved")

    assert issue.status == "Resolved"


# -----------------------------------------
# ANALYTICS TEST
# -----------------------------------------

def test_analytics():

    issues = [

        {
            "id": 1,
            "title": "Broken Fan",
            "location": "Hostel",
            "category": "Maintenance",
            "description": "Fan broken",
            "severity": "High",
            "priority": "Urgent",
            "status": "Resolved"
        },

        {
            "id": 2,
            "title": "WiFi Problem",
            "location": "Library",
            "category": "Network",
            "description": "WiFi slow",
            "severity": "Medium",
            "priority": "Important",
            "status": "Open"
        },

        {
            "id": 3,
            "title": "Broken Chair",
            "location": "Classroom",
            "category": "Maintenance",
            "description": "Chair broken",
            "severity": "Low",
            "priority": "Normal",
            "status": "In Progress"
        }

    ]


    result = calculate_analytics(issues)


    assert result["total"] == 3

    assert result["open"] == 1

    assert result["in_progress"] == 1

    assert result["resolved"] == 1

    assert result["urgent"] == 1

    assert result["resolution_rate"] == 33.33

    assert result["most_common_category"] == "Maintenance"

    assert result["most_common_category_count"] == 2


# -----------------------------------------
# EMPTY ANALYTICS TEST
# -----------------------------------------

def test_empty_analytics():

    result = calculate_analytics([])

    assert result["total"] == 0

    assert result["open"] == 0

    assert result["resolved"] == 0

    assert result["urgent"] == 0

    assert result["resolution_rate"] == 0


# -----------------------------------------
# TEST RUNNER
# -----------------------------------------

def run_tests():

    tests = [

        test_priority_low,
        test_priority_medium,
        test_priority_high,
        test_invalid_priority,

        test_severity_choice,
        test_invalid_severity_choice,
        test_valid_severity,
        test_invalid_severity,

        test_text_validation,
        test_empty_text_validation,
        test_issue_id_validation,
        test_invalid_issue_id,
        test_negative_issue_id,
        test_severity_validation,
        test_invalid_severity_validation,
        test_status_validation,
        test_invalid_status_validation,
        test_confirmation,

        test_issue_creation,
        test_issue_to_dict,
        test_issue_from_dict,
        test_issue_status_update,

        test_analytics,
        test_empty_analytics
    ]


    passed = 0


    print("\n" + "=" * 50)

    print("       FIXMYCAMPUS TEST SUITE")

    print("=" * 50)


    for test in tests:

        try:

            test()

            print("PASS :", test.__name__)

            passed += 1

        except AssertionError:

            print("FAIL :", test.__name__)


        except Exception as error:

            print(
                "ERROR:",
                test.__name__,
                "->",
                error
            )


    print("\n" + "-" * 50)

    print(
        "Tests Passed:",
        passed,
        "/",
        len(tests)
    )


    if passed == len(tests):

        print("Result: ALL TESTS PASSED")


    else:

        print("Result: SOME TESTS FAILED")


    print("=" * 50)


# -----------------------------------------
# START TESTS
# -----------------------------------------

if __name__ == "__main__":

    run_tests()