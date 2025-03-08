#Convert two lists into a dictionary

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
new_dict ={}
for i in range(len(keys)):
    new_dict[keys[i]] = values[i]
    
print(new_dict)

'''
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

res_dict = dict(zip(keys, values))
print(res_dict)

'''