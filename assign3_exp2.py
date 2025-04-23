originalnum = int(input("Enter Your Number to Find the Digital Root: "))

num = originalnum

while num >= 10:  
    sum_of_digits = 0
    while num > 0:
        sum_of_digits += num % 10
        num //= 10
    num = sum_of_digits

print(f"Digital Root = {num}")