
#-------------------------AGE & BIRTHDAY CALCULATOR--------------------------------------------#
"""
                  Project Title : AGE & BIRTHDAY CALCULATOR
                           Name : Likhith 
                          Place : INDIA
"""

from datetime import date
import re


def main():
    birthmonth, birthday, birthyear = is_valid(input("Enter your Birthdate (M/D/,Y): ").lower())
    today = date.today()
    age = calculate_age(birthmonth, int(birthday), int(birthyear), today)
    days = calculate_days(birthmonth, int(birthday), today)
    print(f"Your age as of {date.today().strftime('%B %d, %Y')} is {age} years old.\n{days} days left for your next Birthday!🥳")


def is_valid(birthdate: str):
    regex = r"^([a-z]{3,9})\s([0-2]?[0-9]|3[0-1]),\s?([0-9]{4})$"
    if matches := re.search(regex, birthdate, re.IGNORECASE):
        return matches.group(1), matches.group(2), matches.group(3)
    else:
        raise ValueError("Invalid Format. Please re enter in this Format : 'Month date, year'!")


def month_to_integer(month: str):
    months = {
        "fullname": {"january": 1,"february": 2,"march": 3,"april": 4,"may": 5,"june": 6,"july": 7,"august": 8,"september": 9,"october": 10,"november": 11,"december": 12,},
        "abbreviated_name": {"jan": 1,"feb": 2,"mar": 3,"apr": 4,"may": 5,"jun": 6,"jul": 7,"aug": 8,"sept": 9,"oct": 10,"nov": 11,"dec": 12,},
    }
    if month in months["fullname"]:
        return months["fullname"][month]
    elif month in months["abbreviated_name"]:
        return months["abbreviated_name"][month]
    else:
        raise ValueError("Month not found.")


def calculate_age(birthmonth: str, birthday: int, birthyear: int, today):
    total_age = (today.year - birthyear)
    if month_to_integer(birthmonth) > today.month:
        total_age -= 1
    elif month_to_integer(birthmonth) == today.month:
        if birthday > today.day:
            total_age -= 1
    return total_age


def calculate_days(birthmonth: str, birthday: int, today):
    year_birthday = date(today.year, month_to_integer(birthmonth), birthday)
    if year_birthday < today:
        year_birthday = year_birthday.replace(year=today.year + 1)
    time_to_birthday = abs(year_birthday - today)
    return time_to_birthday.days

if __name__ == "__main__":
    main()
