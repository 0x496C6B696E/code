try:
    n = int(input("Please enter number: ").strip())
    
    if n % 2 == 1:
        print("Weird")
    elif 2 <= n <= 5 and n % 2 == 0:
        print("Not Weird")
    elif 6 <= n <= 20 and n % 2 == 0:
        print("Weird")
    elif n > 20 and n % 2 == 0:
        print("Not Weird")
    else:
        print("Only number!")
        
except ValueError:
    print("Please enter valid number!")