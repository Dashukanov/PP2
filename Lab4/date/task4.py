from datetime import datetime

def date_difference_in_seconds(date1, date2):
    timedelta = date2 - date1
    return abs(timedelta.total_seconds())

def main():
    date1_str = input("Enter the first date (YYYY-MM-DD HH:MM:SS): ")
    date2_str = input("Enter the second date (YYYY-MM-DD HH:MM:SS): ")

    date1 = datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")
    date2 = datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")

    difference_seconds = date_difference_in_seconds(date1, date2)

    print("Difference between the two dates in seconds:", difference_seconds)

if __name__ == "__main__":
    main()
