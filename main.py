from PullGDAXData import get_gdax_historical_data
from DataManipulation import *
from MACDCalculations import *
from RSI import *

### Do we really need the update request or can we do it in main? ###
### Does it aesthetically look better to have it in a separate function? ###


def main():
    '''
    Create functionality where can manually decide to input a datetime to pull data through, or not and move on
    '''
    user_input = input("Please enter a command for the following options.\n'date' If looking to manually update data through a specific date/time\n'auto' To run automatically for a specified chart time interval\n'continue' to perform no updates or automatic pull\n'quit' To quit\nCommand: ")
    status = update_request(user_input)
    if status == 11:
        return "Update successful!"
    elif status == 21:
        print("Running/done running? Depending on how decide to use the automatic run")
    elif status == 31:
        print("We're going to continue!")
        #call function to get working on other functionality of program and return success/failure
    elif status == 41:
        return
    else: #input signal invalid due to invalid user input
        print("Error, invalid signal. Quitting...")
        return

    
def update_request(command):
    if command == "date":
        datetime = input("Please enter the date/time to be updated through (in UTC) in the exact format, 'YYYY-MM-DDTHH:mm:ss+TZD(ex. 1:00 if 1 hour ahead)': ")
        print(datetime)
        #implement try/exception to catch if correct format, if not have continually prompt for a correct format until success
        #If correct, call PullGDAXData and adapt that file to have the last date as an argument in the code where the program passes this user input as the final date once it's correct
        return 11 #11 signifies successful data update request for the first option
    elif command == "auto":
        '''
        eventually implement automatic run here
        '''
        print("Future location for automatic run")
        return 21
        #need to figure out how to make the auto run stop!    
    elif command == "continue":
        return 31
    elif command == "quit":
        return 41    
    else: 
        return "00"
    
main()