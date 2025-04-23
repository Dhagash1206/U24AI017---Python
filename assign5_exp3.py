# Given a word w, rearrange the letters of w to construct another word s in such a way that s is
# lexicographically greater than w.


def next_lexicographic_permutation(w):
    w = list(w)
    n = len(w)
    
    i = n - 2
    while i >= 0 and w[i] >= w[i + 1]:
        i -= 1

    if i == -1:
        return "No further lexicographic order"

    j = n - 1
    while w[j] <= w[i]:
        j -= 1
        
    w[i], w[j] = w[j], w[i]

    w = w[:i + 1] + sorted(w[i + 1:])

    return "".join(w)


word = input("Enter word to check lexicographic order : ")
result = next_lexicographic_permutation(word)
print("Next lexicographic word:", result)
