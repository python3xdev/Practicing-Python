'''
Create a program that asks the user for a number and then prints out a list
of all the divisors of that number.

(If you don’t know what a divisor is, it is a number that divides evenly 
into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
'''
num = int(input("Enter a number:\n"))
results = []

for i in range(1, num + 1):
	if num % i == 0:
		results.append(i)

print(results)

'''
Time taken: 2 minutes
Result:
Enter a number:
4096
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

'''