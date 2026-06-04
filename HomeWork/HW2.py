"""
HW1: Write
a program that takes a string input from the user.
For each character in the string,
creates and prints a new string that is a repetition of the character up to
that index in the original string.
"""
word = input("Enter the sentence: ")
index = 1

for i in word:
    result = i * index
    index += 1
    print(result) 


"""
HW2: Create
a list of integers up to user input.
Calculate average of these numbers.
"""
user = int(input("Enter the number: "))
num_list = []

for i in range(1, user + 1):
    num_list.append(i)

total = sum(num_list)
avg = total / len(num_list)
print(f'Number List:{num_list} Average:{avg}')


"""
HW3: Take
an integer n as input from the user.
Generate a list of tuples, where
each tuple contains an integer and its cube
"""
n = int(input("Enter the number: "))
total = []

for i in range(1, n + 1):
    result = (i, i ** 3)
    total.append(result)
print(total)