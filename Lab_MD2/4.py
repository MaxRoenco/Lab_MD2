string = input("Input string: ")


def is_palindrom(string):
    return string == string[::-1]


def shortest_palindrome(s):
    for i in range(len(s))[::-1]:
        if is_palindrom(s[:i]):
            return s[i:]


first = shortest_palindrome(string)[::-1]
result = "".join(first) + string
print(result)


