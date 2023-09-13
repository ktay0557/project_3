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


def get_miles_data():
    """
    Get the daily miles for each member for the user
    """
    print("Data should be five numbers, separated by commas.")
    print("Example: 12,5,8,6,7\n")
    week = list(calendar.day_name)
    miles_data = {}

    for day in week:
        print(f"Please enter the miles data from {day}, for each member.")
        data_str = input("Enter the data here: ")
        miles_data[day] = data_str

    print("\n")

    for day, data in miles_data.items():
        print(f"The miles provided for {day} are {data_str}")

get_miles_data()
