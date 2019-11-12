from datetime import datetime
from datetime import date
from datetime import time


def main():
    today=date.today()
    print("Today's date is ", today)
    print("Date components",today.day,"-",today.month,today.year)
    print("Todays week day number is",today.weekday())

    days = ["mon","tue","wed","thurs","fri","sat","sun"]

    print(days[today.weekday()])

main()
