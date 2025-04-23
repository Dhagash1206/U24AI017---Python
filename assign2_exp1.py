#Write a program that asks the user to enter a word and then capitalizes every other letter of
#that word. So, if the user enters rhinoceros, the program should print rHiNoCeRoS.

word = input("Enter a word: ")
result = ""
for i in range(len(word)):
    if i % 2 == 0:
        result += word[i].lower()
    else:
        result += word[i].upper()
print(result)
