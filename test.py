def call(num: int, count: int = 0):
    for i in range(num):
        count = call(i, count + 1)
    return count

print(call(int(input())))

# 1, 2, 1
