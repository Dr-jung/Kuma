import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost',27017)
db = client.navermovies
db.users.delete_many({})
movie_infos = []


# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
movies = soup.select('#old_content > table > tbody > tr')

# movies (tr들) 의 반복문을 돌리기
for movie in movies:
    # movie 안에 a 가 있으면,
    a_tag = movie.select_one('td.title > div > a')
    if a_tag is not None:
        # a의 text를 찍어본다.
        rank = movie.select_one('td:nth-child(1) > img')['alt']  # img 태그의 alt 속성값을 가져오기
        title = a_tag.text  # a 태그 사이의 텍스트를 가져오기
        star = movie.select_one('td.point').text  # td 태그 사이의 텍스트를 가져오기
        # print(rank, title, star)
        movie_infos.append({'rank' : rank, 'title' : title, 'star' : star})
        # print(movie_infos)
        # db.users.insert_one({'rank' : rank, 'title' : title, 'star' : star})

db.users.insert_many(movie_infos)
info = db.users.find({},{'_id' : False})
print(info)

# target_movie = []
# target_movie = list(db.users.find_one({'title': '월-E'}, {'_id' : False}))
# target_star = str(target_movie[0]['star'])

# for movie in movies:
#     if movie['star'] == target_star:
#         print(movie['title'])

