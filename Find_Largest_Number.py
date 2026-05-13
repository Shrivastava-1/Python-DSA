lists = [12,2,34,54,10,4]

largest = lists[0]
secondLargest = 0
x = 0
while x < len(lists):
    if lists[x] > largest:
        secondLargest = largest
        largest = lists[x]
    x += 1

print(largest)
print(secondLargest)


# Method Second
second_largest = 0
for i in lists:
    if i > second_largest and i != largest:
        second_largest = i
print(second_largest)