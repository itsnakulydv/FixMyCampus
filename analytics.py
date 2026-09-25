# -----------------------------------------
# FIXMYCAMPUS - ANALYTICS MODULE
# -----------------------------------------


# -----------------------------------------
# CALCULATE CAMPUS ANALYTICS
# -----------------------------------------

def calculate_analytics(issues):

    total = len(issues)

    open_count = 0
    progress_count = 0
    resolved_count = 0
    urgent_count = 0

    categories = {}


    # -----------------------------------------
    # PROCESS EACH ISSUE
    # -----------------------------------------

    for issue in issues:

        # Count status
        if issue["status"] == "Open":
            open_count += 1

        elif issue["status"] == "In Progress":
            progress_count += 1

        elif issue["status"] == "Resolved":
            resolved_count += 1


        # Count urgent issues
        if issue["priority"] == "Urgent":
            urgent_count += 1


        # Count categories
        category = issue["category"]

        if category in categories:
            categories[category] += 1

        else:
            categories[category] = 1


    # -----------------------------------------
    # RESOLUTION RATE
    # -----------------------------------------

    if total > 0:
        resolution_rate = (resolved_count / total) * 100

    else:
        resolution_rate = 0


    # -----------------------------------------
    # MOST COMMON CATEGORY
    # -----------------------------------------

    most_common_category = "None"
    highest_count = 0


    for category in categories:

        if categories[category] > highest_count:

            highest_count = categories[category]

            most_common_category = category


    # -----------------------------------------
    # RETURN ANALYTICS
    # -----------------------------------------

    analytics = {

        "total": total,

        "open": open_count,

        "in_progress": progress_count,

        "resolved": resolved_count,

        "urgent": urgent_count,

        "resolution_rate": round(resolution_rate, 2),

        "most_common_category": most_common_category,

        "most_common_category_count": highest_count,

        "categories": categories

    }


    return analytics


# -----------------------------------------
# DISPLAY ANALYTICS
# -----------------------------------------

def display_analytics(analytics):

    print("\n" + "=" * 50)

    print("              CAMPUS ANALYTICS")

    print("=" * 50)


    if analytics["total"] == 0:

        print("No issues available for analysis.")

        print("=" * 50)

        return


    print("\nTotal Issues       :", analytics["total"])

    print("Open Issues        :", analytics["open"])

    print("In Progress        :", analytics["in_progress"])

    print("Resolved Issues    :", analytics["resolved"])

    print("Urgent Issues      :", analytics["urgent"])


    print(
        "\nResolution Rate    :",
        analytics["resolution_rate"],
        "%"
    )


    print("\nMost Common Category:")

    print(
        analytics["most_common_category"],
        "-",
        analytics["most_common_category_count"],
        "issue(s)"
    )


    print("\nCategory Breakdown:")


    for category in analytics["categories"]:

        print(
            category,
            ":",
            analytics["categories"][category]
        )


    print("\n" + "=" * 50)