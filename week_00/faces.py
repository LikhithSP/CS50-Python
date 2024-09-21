def main():
    text = input()
    result = convert(text)
    print(result)
def convert(text):
    msg1 = text.replace(":)", '🙂')
    msg2 = msg1.replace(":(", '🙁')
    return msg2

main()

