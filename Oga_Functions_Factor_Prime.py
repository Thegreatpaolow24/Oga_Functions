def smallest_factor(n):
    # Verify if the input is less than 2
    if n < 2:
        print("Invalid input. Enter a number greater than or equal to 2.")
        return

    # Identify the smallest factor, excluding 1
    for i in range(2, n + 1):
        if n % i == 0:
            print(f"The smallest factor other than 1 for {n} is {i}.")
            break


def find_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    print(f"Prime numbers in the range {start} to {end}: {primes}")


# Get user input
try:
    choice = int(input("Enter 1 to find the smallest factor or 2 to find prime numbers in a range: "))
    if choice == 1:
        num = int(input("Enter an integer >= 2: "))
        smallest_factor(num)
    elif choice == 2:
        start_range = int(input("Enter the start of the range: "))
        end_range = int(input("Enter the end of the range: "))
        find_primes_in_range(start_range, end_range)
    else:
        print("Invalid choice. Please enter 1 or 2.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
