# The Love-Letter Mystery

def min_operations_to_palindrome(s):
    return sum(abs(ord(s[i]) - ord(s[~i])) for i in range(len(s) // 2))


# Example usage
print(min_operations_to_palindrome("abc"))
print(min_operations_to_palindrome("abcd")) 
print(min_operations_to_palindrome("cba")) 
