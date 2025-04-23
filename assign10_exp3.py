"""A magic square is an N*N grid of numbers in which the entries in each row, column and
main diagonal sum to the same number (equal to N(N^2+1)/2). Create a magic square for
N=4, 5, 6, 7, 8"""


def generate_odd_magic_square(n):
    magic = [[0]*n for _ in range(n)]
    i, j = 0, n // 2
    for num in range(1, n*n + 1):
        magic[i][j] = num
        i, j = (i - 1) % n, (j + 1) % n
        if magic[i][j]:
            i = (i + 2) % n
            j = (j - 1) % n
    return magic

def generate_doubly_even_magic_square(n):
    magic = [[(n*y) + x + 1 for x in range(n)] for y in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            if (i % 4 == j % 4) or ((i % 4 + j % 4) == 3):
                magic[i][j] = n*n + 1 - magic[i][j]
    return magic

def generate_singly_even_magic_square(n):
    half = n // 2
    k = (n - 2) // 4
    sub_square = generate_odd_magic_square(half)

    magic = [[0]*n for _ in range(n)]
    for i in range(half):
        for j in range(half):
            val = sub_square[i][j]
            magic[i][j] = val
            magic[i+half][j+half] = val + half*half
            magic[i][j+half] = val + 2*half*half
            magic[i+half][j] = val + 3*half*half

    for i in range(half):
        for j in range(n):
            if (j < k or j >= n - k or (j == k and i == k)):
                if j < half:
                    magic[i][j], magic[i+half][j] = magic[i+half][j], magic[i][j]
    return magic

def create_magic_square(n):
    if n % 2 == 1:
        return generate_odd_magic_square(n)
    elif n % 4 == 0:
        return generate_doubly_even_magic_square(n)
    else:
        return generate_singly_even_magic_square(n)

# Display results for N=4 to N=8
for n in range(4, 9):
    print(f"\nMagic Square (N={n}):")
    square = create_magic_square(n)
    for row in square:
        print(row)
