from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('memo.html')

@app.route('/memo', methods=['POST'])
def add_memo():
    imageUrl = request.form['imageUrl']
    title = request.form['title']
    titleURL = request.form['titleURL']
    content = request.form['content']
    comment = request.form['comment']
    memo_data = { 'imageUrl' :imageUrl,'title':title,'titleURL':titleURL,'content':content,'comment':comment }

    client = MongoClient('localhost', 27017)
    memo_tbl = client.memo_db.memo

    memo_tbl.insert_one(memo_data)

    result = {'result':'success','msg':'메모등록완료'}
    return jsonify(result)

@app.route('/memo', methods=['GET'])
def get_memo():
    client = MongoClient('localhost', 27017)
    memo_tbl = client.memo_db.memo
    memo_list = list(memo_tbl.find({},{'_id': False}))
    result = {'result' : 'success','msg' : memo_list}
    # { 'result' : 'success', 'msg' = review_list }
    return jsonify(result)


if __name__ == '__main__':
    app.run()
