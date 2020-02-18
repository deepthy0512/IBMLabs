a=input()
a=a.casefold()
rev=reversed(a)
print()
if list(a)==list(rev):
    print("the word is a palindrome")
else:
    print("the word is not palindrome")