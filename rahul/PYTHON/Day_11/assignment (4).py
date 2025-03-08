import json 

data = {'name':'Rahul',
        'surname':'uppuluri',
        'location':'kcl',
        'phn-no':7093169218}

with open("details.json",mode='w',encoding='utf-8') as file:
    json.dump(data,file)
