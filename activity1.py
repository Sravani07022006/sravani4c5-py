#  to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is Even.")
    else:
        print(f"{number} is Odd.")

num = int(input("Enter a number: "))
check_even_odd(num)