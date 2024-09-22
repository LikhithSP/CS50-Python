ans = input("Greeting: ").lower().strip()

if "hello" in ans:
    print("$0")
elif "h" == ans[0]:
    print("$20")
else:
    print("$100")
