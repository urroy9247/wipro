#Update the first set with items that don’t exist in the second set


set1 = {10, 20, 30}
set2 = {20, 40, 50}

print(set1-set2)
print(set1.difference(set2))

'''
set1 = {10, 20, 30}
set2 = {20, 40, 50}

set1.difference_update(set2)
print(set1)
'''