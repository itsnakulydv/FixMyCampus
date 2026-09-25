# -----------------------------------------
# FIXMYCAMPUS - ISSUE MODEL
# -----------------------------------------


class Issue:

    # -----------------------------------------
    # CONSTRUCTOR
    # -----------------------------------------

    def __init__(
        self,
        title,
        location,
        category,
        description,
        severity,
        priority,
        status="Open",
        issue_id=None
    ):

        self.id = issue_id

        self.title = title

        self.location = location

        self.category = category

        self.description = description

        self.severity = severity

        self.priority = priority

        self.status = status


    # -----------------------------------------
    # CONVERT OBJECT TO DICTIONARY
    # -----------------------------------------

    def to_dict(self):

        return {

            "id": self.id,

            "title": self.title,

            "location": self.location,

            "category": self.category,

            "description": self.description,

            "severity": self.severity,

            "priority": self.priority,

            "status": self.status

        }


    # -----------------------------------------
    # CREATE OBJECT FROM DICTIONARY
    # -----------------------------------------

    @classmethod
    def from_dict(cls, data):

        return cls(

            title=data["title"],

            location=data["location"],

            category=data["category"],

            description=data["description"],

            severity=data["severity"],

            priority=data["priority"],

            status=data.get("status", "Open"),

            issue_id=data.get("id")

        )


    # -----------------------------------------
    # UPDATE STATUS
    # -----------------------------------------

    def update_status(self, new_status):

        self.status = new_status


    # -----------------------------------------
    # DISPLAY ISSUE
    # -----------------------------------------

    def display(self):

        print("\n" + "-" * 50)

        print("Issue ID    :", self.id)

        print("Title       :", self.title)

        print("Location    :", self.location)

        print("Category    :", self.category)

        print("Description :", self.description)

        print("Severity    :", self.severity)

        print("Priority    :", self.priority)

        print("Status      :", self.status)

        print("-" * 50)