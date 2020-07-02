import json

data = {
    'name' : 'Connor',
    'sex' : 'boy',
    'age' : 26
}
print(data, type(data)) # <class 'dict'>
data1 = json.dumps(data)
print(data1, type(data1)) # <class 'str'>
data2 = json.loads(data1)
print(data2, type(data2)) # <class 'dict'>
