from pprint import pprint
from datetime import date, timedelta
import time

import requests

#1
#Hulk, Captain America, Thanos
def hero_request():
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url)
    json_resp = response.json()

    hero_dict = {}
    for hero in json_resp:
        if hero['name'] == 'Hulk' or hero['name'] == 'Capitain America' or hero['name'] == 'Thanos':
            hero_name_id = hero['name'] + ' ' + str(hero['id'])
            hero_dict[hero_name_id] = hero['powerstats']['intelligence']

    most_intell_key = max(hero_dict, key = hero_dict.get)
    most_intell_hero_name = most_intell_key.split(' ')[0]
    most_intell_hero_id = most_intell_key.split(' ')[1]

    pprint(f'THe most intelligent hero is {most_intell_hero_name} with id {most_intell_hero_id}')

#3

def minus_two_days():
    today_date = date.today()
    td = timedelta(2)
    time_start = today_date - td
    time_start_unix = time.mktime(time_start.timetuple())
    print(time_start_unix)
    return time_start_unix

def stack_overflow_questions():
    url = 'https://api.stackexchange.com/2.3/questions'
    params = {"order": "desc", "sort": "activity", "site": "stackoverflow", "tagged": "python"}
    response = requests.get(url, params=params)
    json_resp = response.json()
    time_start = minus_two_days()
    for question in json_resp['items']:
        if question['creation_date'] >= time_start:
            pprint(question)

#2
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")

if __name__ == '__main__':
    hero_request()
    disk_file_path = 'send_to_yandex.txt'
    path_to_file = 'send_to_yandex.txt'
    token = ''
    uploader = YaUploader(token)
#    result = uploader.upload_file_to_disk(disk_file_path, path_to_file)

#   pprint(result)
# {'href': 'https://uploader45o.disk.yandex.net:443/upload-target/20220622T194427.959.utd.er5i6x359rbdeciz58j1ecvf2-k45o.226849',
#  'method': 'PUT',
#  'operation_id': '89bdfee869f9b4f94bc841d89e97957038a094dbe8c105c7340741efc3336cf0',
#  'templated': False}
# Success
# None
#    stack_overflow_questions()



