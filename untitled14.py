import requests
import json
url = 'https://www.dcard.tw/service/api/v2/forums/pet/posts?limit=30&before=235776614'
request = requests.get(url)
jsondata = json.loads(request.text)
D = {}
for data in jsondata:
    D['title'] = data['title']
    D['topics'] = data['topics']
    D['gender'] = data['gender']
    D['school'] = data['school']
    with open('wsadwasddwa.json', 'a', encoding='utf-8') as f:
        json.dump(D,f,ensure_ascii=False)
        