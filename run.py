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
    Get the daily miles for each member for the user.
    Run a while loop, collecting valid string of 5 numbers each day,
    separated by commas, from user using the terminal. Repeated until 
    all required valid data is collected.
    """
    print("Data should be five numbers, separated by commas.")
    print("Example: 12,5,8,6,7\n")
    week = list(calendar.day_name)
    mileage_data = {}

    # loops through each day, for mileage from members
    for day in week:
        while True:
            print(f"Please enter the mileage data from {day}, for each member.")
            data_str = input("Enter the data here: ")

            if validate_data(data_str.split(",")):
                mileage_data[day] = data_str
                break
            
    return mileage_data


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
        return False


def get_mileage_only(mileage_data):
    """
    Extracts the mileage from the mileage_data,
    to allow to update the worksheet with just integers.
    """
    mileage_only = [int(mileage) for value in mileage_data.values() for mileage in value.split(",")]
    
    return mileage_only


def update_mileage_worksheet(mileage):
    """
    Update mileage worksheet.
    Add new rows with the daily mileage data collected from user.
    """
    print("Updating mileage worksheet...\n")
    mileage_worksheet = SHEET.worksheet("mileage")

    # ensures new row is added for each day
    for i in range(0, len(mileage), 5):
        row_data = mileage[i:i+5]
        mileage_worksheet.append_row(row_data)

    print("mileage worksheet updated successfully.\n")


def get_weekly_average():
    """
    Collects columns of data from mileage worksheet.
    The last 7 entries for each member, and returns the average
    for each as a list.
    """
    miles = SHEET.worksheet("mileage")

    columns = []
    for ind in range(1, 6):
        column = miles.col_values(ind)
        columns.append(column[-7:])

    return columns


def main():
    """
    Run all the program functions
    """
    data = get_mileage_data()
    mileage_only = get_mileage_only(data)
    mileage = [int(num) for num in mileage_only]
    update_mileage_worksheet(mileage)


print("Hello fellow runners!\n")
# main()

miles_columns = get_weekly_average()
