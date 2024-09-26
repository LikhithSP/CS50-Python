import emoji

user=input("Enter emoji: ")
op=emoji.emojize(user, language='alias')

print(op)
