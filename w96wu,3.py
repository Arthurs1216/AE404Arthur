import requests
from bs4 import BeautifulSoup

postData = {
'_csrf': 'f56a0797-04e8-4cb6-93e6-b1edc800ce65',
'startStation': '1210-新竹',
'endStation': '3390-員林',
'transfer': 'ONE',
'rideDate': '2021/04/24',
'startOrEndTime': 'true',
'startTime': '00:00',
'endTime': '23:59',
'trainTypeList': 'ALL',
'_isQryEarlyBirdTrn': 'on',
'query': '查詢'}
respond = requests.post('https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip112/querybytime',data = postData)
soup = BeautifulSoup(respond.text,'html.parser')
data = soup.find_all('tr', class_ = 'trip-column')
for info in data:
    location = info.find_all('span', class_ = "location")
    location1 = location[0].text
    location2 = location[1].text
    time = info.find_all('td')
    time1 = time[1].text
    time2 = time[2].text
    time3 = time[3].text
    time4 = time[4].text
    print(location1,location2,time1,time2,time3,time4)








