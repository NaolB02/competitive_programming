def swap_case(s):
    swappedS = ''
    for letter in s:
        if letter.islower():
            swappedS += letter.upper()
        elif letter.isupper():
            swappedS += letter.lower()
        else:
            swappedS += letter
    return swappedS

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
