import datetime


def age(date):
    """
    Docstring for age

    :param date: string in form DD-MM-YYYY
    """
    current_date = datetime.datetime.today()
    dt_date = datetime.datetime.strptime(date, "%d-%m-%Y")

    return int((current_date - dt_date).days/365)


date = input("Please enter the age date (DD-MM-YYYY): ")
print(f"The calculated age for {date} is {age(date=date)}")
