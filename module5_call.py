from module5_mod import NumberCollection

def main():
    # Create a new number collection
    collection = NumberCollection()
    
    # Ask the user for input N and validate it
    while True:
        try:
            n = int(input("Enter a positive integer N: "))
            if n <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    
    # Ask the user to provide N numbers and add them to the collection
    print(f"Please enter {n} numbers:")
    for i in range(1, n + 1):
        while True:
            try:
                number = int(input(f"Enter number {i}: "))
                collection.add_number(number)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
    
    # Ask the user for input X
    while True:
        try:
            x = int(input("Enter the number X to search for: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    # Search for X in the collection and output the result
    result = collection.search_number(x)
    print(result)

if __name__ == "__main__":
    main()
