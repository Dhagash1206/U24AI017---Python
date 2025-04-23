def tree(cycle):
    height = 1
    for i in range (1, cycle + 1):
        if i % 2 != 0:
            height *= 2
        else:
            height += 1
    print("The height of the tree after", cycle, "growth cycles is", height)


cycles = []
test = int(input("Enter the number of test cases : "))
for i in range (test):
    print(i + 1)
    a = int(input("Enter the number of growth cycles for this test case: "))
    cycles.append(a)
    
    for cycle in cycles:
        tree(cycle)
