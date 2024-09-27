import random


def main():
    score = 10
    level = get_level()

    for _ in range(10):
        x, y = generate_integer(level)

        i = 0
        while i < 3:
            print(f"{x} + {y} = ", end='')

            try:
                ans = int(input())
            except ValueError:
                print("EEE")
                i += 1
                continue

            if ans != x+y:
                print("EEE")
                i += 1
                continue
            else:
                break

        if i == 3:
            print(f"{x} + {y} = {x+y}")
            score -= 1

    print(f"Score: {score}")

def get_level():

    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue

        if level not in [1, 2, 3]:
            continue
        else:
            return level

def generate_integer(level):

    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)

    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)

    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)

    return x, y


if __name__== "__main__":
    main()
