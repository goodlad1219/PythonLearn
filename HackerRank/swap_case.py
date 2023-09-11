def swap_case(s):
    ls = list(s)
    for i in range (len(s)):
        if (s[i] == s[i].upper()):
            ls[i] = ls[i].lower()
        elif (s[i] == s[i].lower()):
            ls[i] = ls[i].upper()
# or you can use the swapcase() method to do the swapping instead 
    return "".join(ls)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)