'''
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
'''
user_str = input("String Please:\n")
user_str_backwards = user_str[::-1]

if user_str == user_str_backwards:
	print(f"{user_str} is a palindrome.")
else:
	print(f"{user_str} is not a palindrome.")

'''
Time taken: 2 minutes
Result:
Test1:
	String Please:
	civic
	civic is a palindrome.
Test2:
	String Please:
	level
	level is a palindrome.
Test3:
	String Please:
	python
	python is not a palindrome.


'''