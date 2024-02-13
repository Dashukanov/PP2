from datetime import datetime, timedelta

def subtract_days_from_current_date(days):
    current_date = datetime.now()
    subtracted_date = current_date - timedelta(days=days)
    return subtracted_date

five_days_ago = subtract_days_from_current_date(5)

print("Five days ago from the current date:", five_days_ago.strftime("%Y-%m-%d"))
