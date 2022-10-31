
from curses.ascii import isdigit
import imp


MAX_LINES = 5

def deposit():
    while True:
        amount = input("What would you like to deposit?")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else: 
            print("Please enter a number.")
    return amount

def get_number_of_lines():
    while True: 
        lines = input("Enter the number of lines to bet on (1" + str(MAX_LINES)+ ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("The number must be between 1 and " + str(MAX_LINES))
        else: 
            print("Please enter a number")
    return lines


def main():
    balance = deposit()
    lines = get_number_of_lines()
    
main()