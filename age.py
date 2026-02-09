import datetime


def get_current_time():
    return datetime.datetime.today()


def age(date: str) -> int:
    """
    Docstring for age

    :param date: string in form DD-MM-YYYY
    """
    current_date = get_current_time()
    dt_date = datetime.datetime.strptime(date, "%d-%m-%Y")

    return int((current_date - dt_date).days/365)


def check_date(date: str) -> bool:
    """
    Checks for if date string given is in valid format

    :param date: string for date
    """
    date_components = date.split("-")
    # splitting the months to check
    # correct day count in comparison to the month

    short_months = [2, 4, 7, 9, 11]
    february = 2
    if len(date_components) != 3:
        print(f"invalid number of components found in date")
        print(f"should be 3, found {len(date_components)}")
        return False
    day, month, year = date_components
    # ensuring all can be expressed as integers
    try:
        day = int(day)
        month = int(month)
        year = int(year)
    except:
        print("Integer conversion failed")
        return False
    if month > 12 or month < 1:
        print("Month out of range")
        return False
    if day > 31 or day < 1:
        print("Day out of range")
        return False
    # invalid month day combinations
    if month in short_months and day > 30:
        print("Day out of range given month")
        return False
    # leap years
    if month == february:
        if day > 29:
            print("Day out of range given month")
            return False
        if day > 28 and year % 4:  # 29th but not a leap year
            print("Day out of range given month and year")
            return False
    return True


date = input("Please enter the date for calculating age (DD-MM-YYYY): ")
valid_date = check_date(date)
if not valid_date:
    print("Oh no, it looks like you might've put an invalid date in.")
else:
    calculated_age = age(date=date)
    print(f"The calculated age for {date} is {age(date=date)}")
    if calculated_age < 0:
        print("This must be from the future.")
