def linear_sorting(num):
    x = 0
    while x < len(num):
        y = x + 1
        while y < len(num):
            if num[x] > num[y]:
                num[x], num[y] = num[y], num[x]
            y += 1
        x += 1
    return num


def linearSorting(num):
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            if num[i] > num[j]:
                num[i], num[j] = num[j], num[i]
    return num
