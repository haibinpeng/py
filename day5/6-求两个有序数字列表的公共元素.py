list1 = [1, 2, 3, 4, 5]
list2 = [1, 3, 5, 6]
list3 = []
i, j = 0, 0
while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        i += 1
    elif list1[i] < list2[j]:
        j += 1
    else:
        list3.append(list1[i])
        i += 1
        j += 1
print(list3)
