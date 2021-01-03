import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id=None):
    data ={}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url=URL,data = json_data)
    data = r.json()
    print(data)
# fetching for all data to the database in jsong form 
get_data() 

def post_data():
    data = {
        'name':'Manish',
        'roll':523,
        'city':'dipanjali'
    }
    json_data =json.dumps(data)
    r = requests.post(url=URL,data = json_data)
    data = r.json()
    print(data)
# insert data into backend with the help ho client json dta
# post_data() 

def update_data():
    data = {
        'id':3,
        'name':'shikha',
        'city':'Lucknow'
    }

    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)

# update_data()

def delete_data():
    data = {'id':3}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)

# delete_data()