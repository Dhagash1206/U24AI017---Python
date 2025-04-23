# You are given a number N, you need to print the number of positions where digits exactly
# divides N.

test_cases = int(input("Enter the number of test cases : "))
L = []
for i in range(test_cases):
    a = int(input("Enter the number : "))
    L.append(a)
print(L)

for i in L:
    temp = i
    count = 0
    while i > 0:
        num = i % 10
        i = int(i / 10)
        if num != 0:
            if temp % num == 0:
                count += 1
    print(count) 
