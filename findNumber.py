def find_number():
    lists = []
    for i in range(5):
        num = int(input("Enter number : "))
        lists.append(num)

    count = 0
    user_num = int(input("Enter number to search : "))
    for i in lists:
        if user_num == i:
            found = True
            find = i
            index = lists.index(i)
            count += 1
        elif user_num != i:
            found = False

    if found:
        print(f"Found Number {find} at index {index} and the count is {count}")
    else:
        print("Not Found")