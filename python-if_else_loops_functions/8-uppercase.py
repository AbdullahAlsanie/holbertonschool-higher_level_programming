#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in range(len(str)):
        char = str[i]
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            result += chr(ord(char) - 32)
        else:
            result += char
    print(f"{result}")
