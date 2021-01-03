import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id=None):
    data ={}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}
    r = requests.get(url=URL,headers=headers,data = json_data)
    data = r.json()
    print(data)
# fetching for all data to the database in jsong form 
get_data() 

def post_data():
    data = {
        'name':'harshit',
        'roll':102,
        'city':'nepal'
    }
    json_data =json.dumps(data)
    headers = {'content-Type':'application/json'}
    r = requests.post(url=URL,headers=headers,data = json_data)
    data = r.json()
    print(data)
# insert data into backend with the help ho client json dta
# post_data() 

def update_data():
    data = {
        'id':4,
        'name':'mohit',
        'city':'himalaya'
    }

    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}
    r = requests.put(url=URL,headers=headers, data=json_data)
    data = r.json()
    print(data)

# update_data()

def delete_data():
    data = {'id':4}

    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.delete(url=URL,headers=headers, data=json_data)
    data = r.json()
    print(data)

# delete_data()