def fibonacci(idx):
    if idx <= 0:
        return 0
    if idx == 1:
        return 1

    a, b = 0, 1
    for i in range(2, idx + 1):
        a, b = b, a + b
    return b


result = fibonacci(3)
print(result)
