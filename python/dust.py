import requests
from bs4 import BeautifulSoup

KEY = 'pxMYp9JSAcMSOWwfcT71Z8sOqMrNPrQqbdZwIbx03u8bzY65gKa8oDNXF1ACao8V6NJAFFPFTdFK3ojdHq%2BR4A%3D%3D'
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={KEY}&numOfRows=10&pageNo=3&sidoName=서울&ver=1.0'
# print(url)
response = requests.get(url).text
data = BeautifulSoup(response, 'xml')
# print(data)
item = data('item')[7]
time = item.dataTime.text
station = item.stationName.text
dust = int(item.pm10Value.text)

print(f'{time} 기준 {station}의 미세먼지 농도는 {dust} 입니다.')


if dust > 150:
    print('매우나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')