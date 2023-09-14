import gspread
from google.oauth2.service_account import Credentials
import calendar

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('felling_running_club')


def get_mileage_data():
    """
    Get the daily miles for each member for the user
    """
    print("Data should be five numbers, separated by commas.")
    print("Example: 12,5,8,6,7\n")
    week = list(calendar.day_name)
    mileage_data = {}

    for day in week:
        while True:
            print(f"Please enter the mileage data from {day}, for each member.")
            data_str = input("Enter the data here: ")

            if validate_data(data_str.split(",")):
                mileage_data[day] = data_str
                break
            else:
                print("Please enter valid quanity of miles.")
        

    print("\n")

    for day, data in mileage_data.items():
        print(f"The mileage provided for {day} are {data_str}")


def validate_data(values):
    """
    Inside try, will convert the string values into integers.
    If strings cannot be converted, or if there is not 5 values,
    will raise a ValueError.
    """
    try:
        if len(values) != 5:
            raise ValueError(
                f"5 values are required, you gave {len(values)}"
            )

        [int(value) for value in values]
        return True

    except ValueError as e:
        print(f"Invalid miles: {e}, please try again.\n")


get_mileage_data()
