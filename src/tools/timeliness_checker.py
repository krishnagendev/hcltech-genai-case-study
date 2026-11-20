from datetime import datetime


def timeliness_checker(submission_date, trip_start_date):

    submitted = datetime.strptime(
        submission_date, "%Y-%m-%d"
    )

    trip_start = datetime.strptime(
        trip_start_date, "%Y-%m-%d"
    )

    days_difference = (submitted - trip_start).days

    return {
        "days_difference": days_difference,
        "valid": 0 <= days_difference <= 30
    }