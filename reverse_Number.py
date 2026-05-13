def reverse_number(lists):

    x = 0
    y = len(lists) - 1

    while x < y:
        lists[x], lists[y] = lists[y], lists[x]
        x += 1
        y -=1
    return lists

num = [2,21,21,1,12,21,123,32,2,12,32,-1]
user = reverse_number(num)
print(user)