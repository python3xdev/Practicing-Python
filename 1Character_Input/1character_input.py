'''
 Create a program that asks the user to enter their name and their age.
 Print out a message addressed to them that tells them the year that they will turn 100 years old.

 Extras:

	Add on to the previous program by asking the user for another number
	and printing out that many copies of the previous message. (Hint: order of operations exists in Python)

	Print out that many copies of the previous message on separate 
	lines. (Hint: the string "\n is the same as pressing the ENTER button)
'''
from datetime import date

name = input("Please enter your name:\n")
age = int(input("Please enter your age:\n"))
times = int(input("How many times would you like to print it out?:\n"))

print(f"{name} will be 100 years old in the year of {date.today().year+(100-age)}.\n" * times)

'''
I first started with hardcoding the 2021 year into a variable,
but then I used the datetime module to make this program work in any given year.

Time taken: 1 minute
'''