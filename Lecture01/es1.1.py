"""

    Write a program that reads an integer given as input from the user and determines whether it is divisible by 2, 3, 5, or 7.

    Encapsulate the check into a function taking as input two numbers, and write a program that asks the user to insert two numbers and checks whether the first is divisible by the other one (and vice-versa).
"""
def checkDivisors (x, y):
    if x % y == 0 :
        print(f"{x} is divisible by {y}")
    else : print(f"{x} is not divisible by {y}")


a = int( input("Provide an integer: "))

divisors = [2,3,5,7]

for i in divisors:
    checkDivisors(a, i)


num = [input("Provide the first number : " ), input("Povide the second numeber :" )]

checkDivisors(int(num[0]), int(num[1]))
