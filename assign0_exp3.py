# find the factorial of a number using python

num = int(input("enter first number : "))

fact = 1

for i in range(1, num + 1):

    fact *= i
    
print("Factorial of the number is : ", fact)
