def bubble_sort(lists):
    x = len(lists) - 1
    while x > 0:
        y = 0
        while y < x:
            if lists[y] > lists[y+1]:
                lists[y], lists[y+1] = lists[y+1], lists[y]
            y += 1
        x -= 1
    print(lists)

data = [1,23,21,14,3,54]
user = bubble_sort(data)