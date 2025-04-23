def is_fibonacci(num):
    a, b = 0, 1
    while b <= num:
        if b == num:
            return True
        a, b = b, a + b
    return False

num = int(input("Enter a number of choice: "))

if is_fibonacci(num):
    print(f"{num} is a Fibonacci number")
else:
    print(f"{num} is not a Fibonacci number")
