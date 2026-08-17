
def first_non_repeating(s):
    count = {}
    for ch in s:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1
    for ch in s:
        if count[ch] == 1:
            return ch
    return -1
s = input()
print(first_non_repeating(s))