
import re
import sys

def main():
    print(validate(input("IPV4 Address: ")))

def validate(ip):
    if match_ip := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$",ip):
        if int(match_ip.group(1)) <=255 and int(match_ip.group(2)) <=255 and int(match_ip.group(3)) <=255 and int(match_ip.group(4)) <=255:
            return True
        else:
            return False

    else:
        return False

if __name__ == "__main__":
    main()
