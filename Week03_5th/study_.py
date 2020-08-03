import requests

air_infos = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
air_infos_dictionary = air_infos.json()
print(air_infos_dictionary['RealtimeCityAir']['row'])
