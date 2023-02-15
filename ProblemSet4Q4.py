# Aryan Gidwani
# November 12, 2021
# ICS3UO - A
# The purpose of this program is to form a programming necklace. The user will
# input two numbers, and will then add those numbers. It will print out the
# unit's digit of the sum of the two numbers. This process will continue until
# the two starting numbers are reached once again.

name = input("Hello! What is your name? ")
# asks the user for their name
print("Hello " + name + "! Hope you are having a nice day. The purpose of this program is to " + "\n" + " add two user-inputted numbers and find the units digit of the sum. This process" + "\n" + " will be continued until the one's digits that the program started with will " + "\n" + " appear at the end!")
# introductory message
firstNumber = float(input("All numbers will be rounded and will be changed into its' positive counterpart. Enter in a single digit number: "))
# asks the user for the first number of their choice
firstNumber = abs(round(firstNumber))
# rounds the number and takes the absolute value of it
secondNumber = float(input("Enter in your second, single-digit number: "))
# asks the user for the second number
secondNumber = abs(round(secondNumber))
# rounds the number and takes the absolute value of it
while (firstNumber >= 10) or (secondNumber >= 10):
    print("Input single digit numbers please!")
    # invalid input message
    firstNumber = float(input("All numbers will be rounded and will be changed into its' positive counterpart. Enter in a single digit number: "))
    # asks the user for the first number of their choice
    firstNumber = abs(round(firstNumber))
    # rounds the number and takes the absolute value of it
    secondNumber = float(input("Enter in your second, single-digit number: "))
    # asks the user for the second number
    secondNumber = abs(round(secondNumber))
    # rounds the number and takes the absolute value of it

print("Step 1: " + str(firstNumber))
# prints the first number inputted
print("Step 2: " + str(secondNumber))
# prints the second number inputted
fixedNumberOne = firstNumber
# stores the original value in a fixed variable fixedNumberOne
fixedNumberTwo = secondNumber
# stores the original value in a fixed variable fixedNumberTwo
unitsDigit = (firstNumber + secondNumber) % 10
# finds the units digit of the sum of the two numbers; this is done outside of
# the loop to change the values once so that the while loop can function
firstNumber = secondNumber
# updates and changes the value of the first number to the second number
secondNumber = unitsDigit
# changes the value of the variable secondNumber to the units digit of
# the sum of the two numbers
print("Step 3: " + str(unitsDigit) + " is the unit's digit of the sum of the two previous numbers.")
# prints the unit digit of the sum of the numbers
totalSteps = 3
# stores the original value for the total steps when it enters the loop

while (firstNumber != fixedNumberOne) or (secondNumber != fixedNumberTwo):
    unitsDigit = (firstNumber + secondNumber) % 10
    # finds the units digit of the sum of the two numbers
    firstNumber = secondNumber
    # updates and changes the value of the first number to the second number
    secondNumber = unitsDigit
    # changes the value of the variable secondNumber to the units digit of
    # the sum of the two numbers
    totalSteps = totalSteps + 1
    # updates the total number of steps it takes to get to the original numbers
    print("Step " + str(totalSteps) + ": " + str(unitsDigit) + " is the unit's digit of the sum of the two previous numbers.")
    # prints the units digit of the sum of the numbers

print("It takes " + str(totalSteps) + " total steps to reach the original, starting number! The necklace is complete! Thank you for using this program!")
# concluding message
