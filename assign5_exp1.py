"""MAXimizing XOR
Given two integers: L and R, Find the MAXimal values of A xor B"""


def find_MAX_XOR(A, B):
    MAX = 0
    for i in range(A, B + 1):
        for j in range(i, B + 1): 
            element = i ^ j
            if element > MAX:
                MAX = element
    return MAX


A = int(input("Enter the value of A: "))
B = int(input("Enter the value of B: "))
MAX = find_MAX_XOR(A, B) 

print(f"The MAXimal value of A xor B is : {MAX} ")
