vowels = ["A", "E", "I", "O", "U"]
twitter = input("Input: ")

for letter in twitter:
    if chr(ord(letter) - 32) in vowels or letter in vowels:
        twitter = twitter.replace(letter, "")
print(twitter)

