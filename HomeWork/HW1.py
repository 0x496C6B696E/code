"""
HW1: Create
a list of the squares of numbers from 10 to 15.
Extract and print the last three
elements of this list.
"""
print([i ** 2 for i in range(10, 16)][-3:])


"""
HW2: Write
a Python program that:
Asks the user to input three words.
Combines these words into a single string, with each word separated by a hyphen ('-').
Asks the user to enter a number m.
Prints the combined string m times.
"""
user1 = input("Enter the first word: ")
user2 = input("Enter the second word: ")
user3 = input("Enter the last word: ")
m = int(input("Repeat: "))
print(f"({user1}-{user2}-{user3})\n" * m)


"""
HW3: 
You have a list numbers = [2,3,5,7,11,13,17,19,23,29,31]. 
Create a new list that contains every third element from the original list.
"""
number = [2,3,5,7,11,13,17,19,23,29,31]
new_list = number[2::3] 
print(new_list)


"""
HW4: You
have a list numbers = [2,4,6,8,10,12,14,16,18,20]. For each number in your
list, first square it, then multiply the squared value by 3, and finally
subtract 1 from this product.
"""
numbers = [2,4,6,8,10,12,14,16,18,20]

# 4.1
for i in numbers:
    result = ((i ** 2) * 3) - 1
    print(result, end=" ")

# 4.2
print([((i ** 2) * 3) - 1 for i in numbers])


"""
HW5: You
have a list elements = [ [1, 2, 3, 4],['a', 'b', 'c', 'd'],[5.1, 6.2, 7.3,
8.4],['apple', 'banana', 'cherry', 'date'],[True, False, True, False],[9,
'mixed', 10.5, None],['x', 25, 0.1, ['nested', 'list']]]. For each list
concatenate string 'Third element is: ' with third
element of list.
"""
elements = [
    [1, 2, 3, 4],
    ['a', 'b', 'c', 'd'],
    [5.1, 6.2, 7.3, 8.4],
    ['apple', 'banana', 'cherry', 'date'],
    [True, False, True, False],
    [9, 'mixed', 10.5, None],
    ['x', 25, 0.1, ['nested', 'list']]
]

print([f'=>Third element is: {i[2]}<=' for i in elements])


"""
# HW6: Given
# the list elements as defined earlier print reverse of each inner list.
"""
print([j[::-1] for j in elements])