list = [1, 3, 5, 6, 3, 8, 9, 3, 1, 6, 4, 9]

dup_item = set()
same_item = []

for i in list:

    if i not in dup_item:

        same_item.append(i)
        dup_item.add(i)

print("Remove the Duplicate Items:\n", dup_item)