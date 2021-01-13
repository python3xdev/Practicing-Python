'''
Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user. Hint: how does an even / odd
number react differently when divided by 2?

Extras:

    If the number is a multiple of 4, print out a different message.

    Ask the user for two numbers: one number to check (call it num) and
    one number to divide by (check). If check divides evenly into num, 
    tell that to the user. If not, print a different appropriate message.
'''
num = int(input("Enter a number:\n"))
check = int(input("Enter a number to devide by:\n"))

if num % check == 0:
	print(f"{num} is a multiple of {check}.")
else:
	print(f"{num} modulated by {check} returns {num % check}")

'''
I was not quite sure if this was what they asked to do, but I think this is correct.

Time taken: 1.5 minutes
'''