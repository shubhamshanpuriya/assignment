def find_missing_number(numbers):
    n = len(numbers)

    total = 0
    for i in range(1, n + 2):
        total = total + i

    for number in numbers:
        total = total - number

    return total


numbers = list(map(int, input().split()))

result = find_missing_number(numbers)

print(result)