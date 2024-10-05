from datetime import date
import inflect
import sys
import re

def main():
    inpt=input('Date of Birth: ')
    print(get_min(inpt))


def get_min(inpt):
    if search := re.search(r'^(\d{4})-(\d{2})-(\d{2})$',inpt):
        inpt=list(search.groups())
    else:
        sys.exit('Invalid date')

    inpt_bday = convert_and_check(inpt)
    today = date.today()
    bday = date(inpt_bday[0], inpt_bday[1], inpt_bday[2])
    diff = bday - today
    no_of_days = -int(diff.days)
    minutes = no_of_days * 24 * 60
    inf = inflect.engine()
    min_words = inf.number_to_words(minutes)
    min_words = min_words.replace(' and','').capitalize()
    return min_words + ' minutes'


def convert_and_check(day):
    day = list(map(int, day))
    if day[1] < 0 or day[1] > 12:
        sys.exit('Invalid date')
    elif day[2] < 0 or day[2] > 31:
        sys.exit('Invalid date')
    return day

if __name__ == "__main__":
    main()
