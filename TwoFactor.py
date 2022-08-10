##
# @Author: Ed Ardolino
# @Version: 1.0
# @Creation Date: 8-10-2022
##

##
#
# Twofactor.py is a program that generates an 8 factor code that is sent to a cell phone and can be used for
# authentication
#
##

# Imports needed for project
import random


# Starts the program
def start():
    update()


# Function to run the code every 60 seconds until stopped
def update():
    import time
    while True:
        generate_code()
        time.sleep(60)


# Generates a random 8-digit code, casts code to a string and prints it out
def generate_code():
    code = random.choice(range(10000000, 99999999))
    print("Two-Factor Code: " + str(code))


def sms():
    print("Work in progress")


def encryption():
    print("Work in progress")


def authentication():
    print("Work in progress")
