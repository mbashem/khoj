import json

import requests
#
# URL = "http://127.0.0.1:8000/stuinfo"
#
# r = requests.get(url=URL)
#
# data = r.json()
#
# print(data)


# URL = "http://127.0.0.1:8000/stucreate/"
# data = {
#     'name' : 'Omi',
#     'roll' : 100,
#     'city' : 'Cox Bazar'
# }
#
# json_data = json.dumps(data)
#
# r = requests.post(url=URL, data = json_data)
#
# data = r.json()
#
# print(data)


URL = "http://127.0.0.1:8000/stuapi/"

def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id' : id}

    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)


get_data()
#
# def post_data():
#     data = {
#         'name' : 'Omi Farhan Ishraq',
#         'roll' : 500,
#         'city' : 'Cox Bazar'
#     }
#
#     json_data = json.dumps(data)
#
#     r = requests.post(url=URL, data = json_data)
#
#     data = r.json()
#
#     print(data)
#
# post_data()


# def update_data():
#     data = {
#         'id' : 5,
#         'name' : 'Shakib AL Hasan',
#         'city' : 'Cox Bazar'
#     }
#
#     json_data = json.dumps(data)
#
#     r = requests.put(url=URL, data = json_data)
#
#     data = r.json()
#
#     print(data)
#
# update_data()



# def delete_data():
#     data = {
#         'id' : 5
#     }
#
#     json_data = json.dumps(data)
#
#     r = requests.delete(url=URL, data = json_data)
#
#     data = r.json()
#
#     print(data)
#
#
# delete_data()

