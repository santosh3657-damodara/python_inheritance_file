import requests
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'
import json
# def get_resourse(id=None):
#     data={}
#     if id is not None:
#         data={
#             'id':id
#         }
#         resp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
#         print(resp.status_code)
#         print(resp.json())
# get_resourse()
# def create_resource():
#     new_stu = {
#         'sname': 'nagendr',
#         'rollno': '106',
#         'marks': 88,
#         'college': 'nagragunaa college',
#         'gf': 'nimitha',
#         'bf':'ravi'
#     }
#     resp = requests.post(BASE_URL + ENDPOINT, data=json.dumps(new_stu))
#     print(resp.status_code)
#     print(resp.json())
# create_resource()
# def update_resourse(id):
#     new_data = {
#         'id': id,
#         'gf': 'kamala',
    
#     }
#     resp = requests.put(BASE_URL+ENDPOINT , data=json.dumps(new_data))
#     print(resp.status_code)
#     print(resp.json())   
# # id=input('enter some id:')
# update_resourse(4)

def delete_resourse(id):
    data={
        'id':id
    }
    resp = requests.put(BASE_URL+ENDPOINT , data=json.dumps(data))
    print(resp.status_code)
    print(resp.json()) 
delete_resourse(2)
