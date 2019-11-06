string = input("Enter a clear messang: ")
word = string [::-1]
print(*reversed(word.split()))