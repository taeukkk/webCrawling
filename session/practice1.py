import re
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
    
headers = {
# 'Host': 'www.opinet.co.kr',
# 'Origin': 'https://www.opinet.co.kr',
# 'Referer': 'https://www.opinet.co.kr/searRgSelect.do',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}

session = requests.Session()
session.get("https://www.opinet.co.kr/user/main/mainView.do")
response = session.post("https://www.opinet.co.kr/searRgSelect.do",headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
oil_station = []
areas = []
for gu in soup.select('#SIGUNGU_NM0 option'):
    if gu['value']:
        areas.append(gu['value'])
    
for area in areas:
    print(area)
    data = {
        'BTN_DIV': 'os_btn',
        'BTN_DIV_STR': '',
        'POLL_ALL': 'all',
        'SIDO_NM': '서울특별시',
        'SIGUNGU_NM': area,
        'SIDO_CD': '01',
        'SIGUN_CD': '0104',
        'MAP_CENTER_X': '', 
        'MAP_CENTER_Y': '',
        'MAP_ZOOM': '',
        'MAP_FIRST_X': '',
        'MAP_FIRST_Y': '',
        'LPG_YN': '', 
        'SESSION_USER_ID': '', 
        'SIDO_NM0': '서울특별시',
        'SIGUNGU_NM0': area,
        'DONG_NM': '',
        'GIS_X_COOR': '', 
        'GIS_Y_COOR': '', 
        'GIS_X_COOR_S': '', 
        'GIS_X_COOR_E': '', 
        'GIS_Y_COOR_S': '',
        'GIS_Y_COOR_E': '',
        'SEARCH_MOD': 'addr',
        'OS_NM': '',
        'OS_ADDR': '',
        'NORM_YN': 'on',
        'SELF_DIV_CD': 'on',
        'VLT_YN': 'on',
        'KPETRO_YN': 'on',
        'KPETRO_DP_YN': 'on',
        'POLL_DIV_CD': 'SKE',
        'POLL_DIV_CD': 'GSC',
        'POLL_DIV_CD': 'HDO',
        'POLL_DIV_CD': 'SOL',
        'POLL_DIV_CD': 'RTO',
        'POLL_DIV_CD': 'ETC'
    }

    response = session.post("https://www.opinet.co.kr/searRgSelect.do", data=data, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    for data in soup.select("table.tbl_type10 tbody#body2 > tr"):
        items = list(re.finditer("'[^']*',",data.select_one("a").attrs['href']))
        oil_station.append({
            '지역':area,
            '유가':items[2].group(),
            '주유소명':items[22].group(),
            '브랜드':items[23].group(),
            '주소':items[25].group(),
            '셀프주유소여부':items[19].group()
        })
    
for os in oil_station:
    print(os)

df = pd.DataFrame(oil_station)
# print(df)
df['유가'] = df['유가'].astype('int')
# print(df['유가'].isnull().sum())
# print(df[df['유가']==0])

print(df.groupby('셀프주유소여부').min('유가'))
print(df.groupby('지역').min('유가'))
print(df.sort_values(by="유가").head(5)) #저렴한 순서
print(df.sort_values(by="유가",ascending=False).head(5)) #비싼 순서