import json

py_data={'name':"Jatin",'age':True,'''active''':False,"anyother":None}
json_date=json.dumps(py_data)
print(json_date)
print(type(json_date))

j='{"name": "Jatin", "age": "true", "active": "false", "anyother": "null"}'
print(type(j))


py_data=json.loads(j)
print(py_data)
print(type(py_data))