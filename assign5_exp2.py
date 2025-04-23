# Hallow party


def max_chocolate_pieces(K):
    return (K // 2) * ((K + 1) // 2)




T = int(input().strip()) 
for _ in range(T):
    K = int(input("Enter the value of K: ").strip())
    if K > 0:
        print(max_chocolate_pieces(K))
    else:
        print("K must be a positive integer")
