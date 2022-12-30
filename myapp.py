import requests
import json

URL="http://127.0.0.1:8000/student_api/"

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    jason_data=json.dumps(data)
    r=requests.get(url=URL,data=jason_data)
    data=r.json()
    print(data)

# get_data(1)

def post_data():
    data={
        'id':8,
        'name':'Ramesh',
        'roll':44,
        'city':'Pune'
    }
    jason_data=json.dumps(data)
    r=requests.post(url=URL,data=jason_data)
    data=r.json()
    print(data)

post_data()