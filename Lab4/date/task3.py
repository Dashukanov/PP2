from datetime import datetime, timezone, timedelta

def drop_microseconds(dt):
    return dt.replace(microsecond=0)

def main():

    current_datetime_utc = datetime.now(timezone.utc)

    timezone_utc6 = timezone(timedelta(hours=6))
    current_datetime_utc6 = current_datetime_utc.astimezone(timezone_utc6)

    stripped_datetime_utc6 = drop_microseconds(current_datetime_utc6)

    print("Original datetime (UTC +6):", current_datetime_utc6)
    print("Datetime in UTC +6 with microseconds dropped:", stripped_datetime_utc6)

if __name__ == "__main__":
    main()
