# AGE & BIRTHDAY CALCULATOR
#### Description:
This Python program prompts user for their birthdate as input in `Month Day, Year` format,
It prints out their age for the present day and also how many days left till their next birthday.

#### How the Program Works?
It uses python built-in library like `Datetime`[^1] and import `date` object.
To acquire the current local date, `.today()` class method from `date` was used which has `.day`, `.month`, and `.year` instance attributes.

The Program also utilizes the python built-in library `re`[^2] or `regular expression`. This library was used to check the format of the inputted birthdate and extracts the neccesarry data.

To calculate the age, subtract the birthyear from the current year.

The calculations of the age are based on the following factors:
1. If the birthmonth is greater than today's month, this means that the user has not yet celebrated his/her birthday (Example: Birthday is on October[10] and today's month is August[08]). Decrement 1 on age.

2. If the birthmonth and today's month is equal, check if the birthday is greater than today's day. This means that the user has not yet celebrated his/her birhtday (Example: Birthday is on August 25 and today's day is August 17). Decrement 1 on age.

To calculate the days before birthdate, subtract today's date from the birthdate in current year (Example: 2023, 10, 20 - 2023, 08, 19).
1. If the birthday in current year is less than today's date (Example: Birthdate 2023, 02, 11; Today's date 2023, 08, 19) then, increment 1 to the birthyear. This will replace to 2024, 02, 11 - 2023, 08, 19.

### TODO:
#### Download
Download the Repository through Clone Repository or Download Zip

#### Installation
After download, go to `cmd` and navigate to the project folder directory.
```
cd final-project
```
Use [pip](https://pip.pypa.io/en/stable/) to install needed libraries.
```
$ pip install -r requirements.txt
```
#### Usage
Run the program python script `project.py` with [python](https://www.python.org/).
```
python project.py
```
Test the program python script `test_project.py` with [pytest](https://docs.pytest.org/en/7.2.x/).
```
pytest test_project.py
```
After successfully running the program, it will prompt for a birthdate.
Enter the birthdate by following the given format `Month Day, Year`.

That's It. It tells you the age of present day and how many days till your next birthday

>[!NOTE]
>This program is case-insensitive.
>Do not forget the comma `,` between the `day` and `year` of the birthdate.

## References
[^1]: [Datetime library](https://www.w3schools.com/python/python_datetime.asp)
[^2]: [re library](https://www.w3schools.com/python/python_regex.asp)
