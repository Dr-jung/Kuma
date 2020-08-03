from pymongo import MongoClient

client = MongoClient('localhost',27017)
# todo dbsparta라는 database를 찾아라 없다면 만들어라
db = client.dbsparta
# todo dbsparta라는 database에서 users라는 Collection에 다가 {'name' : 'age'}라는 딕션어리를 만들라
# todo 없으면 말ㄴ들라

# db.users.insert_one({'name': '덤블도어', 'age': 116, 'sex' : '남자'})
# db.users.insert_one({'name': '맥고나걸', 'age': 85})
# db.users.insert_one({'name': '스네이프', 'age': 60})
# db.users.insert_one({'name': '해리', 'age': 40})
# db.users.insert_one({'name': '허마이오니', 'age': 40})
# db.users.insert_one({'name': '론', 'age': 40})


# todo False True를 이용하여 받아올 디비를 결정
wizard_infos = list(db.users.find({},{'_id' : False}))
# print(wizard_infos)
db.users.delete_many({})

for wizard_info in wizard_infos:
    print(wizard_info['name'])

# MongoDB에서 특정 조건의 데이터 모두 보기
same_ages = list(db.users.find({'age': 40}))

for user in same_ages:  # 반복문을 돌며 모든 결과값을 보기
    print(user)

# 오타가 많으니 이 줄을 복사해서 씁시다!
db.users.update_one({'name': '덤블도어'}, {'$set': {'age': 200}})

user = db.users.find_one({'name': '덤블도어'})
print(user)
