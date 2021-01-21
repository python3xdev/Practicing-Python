'''
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the
elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.

Extras:

    Randomly generate two lists to test this
    Try to write this in one line (don’t worry if you can’t figure
    this out at this point - we’ll get to it soon).
    (idk how to do this in one line)
'''
from random import randint

a = []
b = []

for x in range(0, 20):
	a.append(randint(0, 100))
	b.append(randint(0, 100))

result = list(set(a).intersection(b)) # this line will work with same or different length lists

print(result)

'''
Time taken: 7 minutes
Result:
(returns the common values from 2 randomly generated lists)
Test1: [7, 45, 79, 48, 84]
Test2: [68, 57, 58, 60, 62]
Test3: [68, 53]
Test4: [32, 4, 100, 11, 25, 26]
Test5: [98, 2, 76, 81, 50, 28]

'''