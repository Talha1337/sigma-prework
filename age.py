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


def check_date(date: str) -> list:
    """
    Checks for if date string given is in valid format

    :param date: string for date

    Output is [True/False for validity, corresponding error message if false]
    """
    date_components = date.split("-")
    # splitting the months to check
    # correct day count in comparison to the month

    short_months = [2, 4, 7, 9, 11]
    february = 2
    # Checking for 3 parts (dd, mm, yyyyy)
    if len(date_components) != 3:
        return False, f"invalid number of components found in date. Should be 3, found {len(date_components)}"
    day, month, year = date_components
    # ensuring all can be expressed as integers
    try:
        day = int(day)
        month = int(month)
        year = int(year)
    except:
        return False, "Integer conversion failed"
    if month > 12 or month < 1:
        return False, "Month out of range"
    if day > 31 or day < 1:
        return False, "Day out of range"
    # invalid month day combinations
    if month in short_months and day > 30:
        return False, "Day out of range given month"
    # leap years
    if month == february:
        if day > 29:
            return False, "Day out of range given month"
        if day > 28 and year % 4:  # 29th but not a leap year
            return False, "Day out of range given month and year"
    return True, "Date is valid"


def test_check_date():
    candidate_dates_and_outcomes = {
        "03141341": False,  # no split
        "09-033/33": False,  # not dash splits
        "40-01-2025": False,  # day out of range
        "05-13-1994": False,  # month out of range
        "1.5-6.4-2026": False,  # day and month are not integers
        "29-02-2024": True,  # valid date (leap year)
        "29-02-2023": False,  # invalid date (not leap year)
    }
    for date in candidate_dates_and_outcomes:
        if candidate_dates_and_outcomes[date] != check_date(date)[0]:
            print(f"Unexpected output from {date}")
            return False
    print("All tests passed")
    return True


test_check_date()

date = input("Please enter the date for calculating age (DD-MM-YYYY): ")
valid_date_and_info = check_date(date)
if not valid_date_and_info[0]:
    print(
        f"Oh no, it looks like you might've put an invalid date in ({valid_date_and_info[1]}).")
else:
    calculated_age = age(date=date)
    print(f"The calculated age for {date} is {age(date=date)}")
    if calculated_age < 0:
        print("This must be from the future.")
