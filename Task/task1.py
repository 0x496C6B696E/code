# TASK 1
n = int(input("Enter the number: "))

if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)


# TASK 2
list1 = int(input("Enter the number of elements: "))
list2 = []

for i in range(list1):
    element = input(f"Enter elemet {i + 1}: ")
    if element not in list2:
        list2.append(element)
print(f"List: {list2}")


# TASK 3
cumle = input("Cumle yaz: ")
soz = {}

for i in cumle.split():
    soz[i] = len(i)
print(soz)