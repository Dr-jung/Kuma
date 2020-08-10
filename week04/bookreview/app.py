from flask import Flask, render_template, request, jsonify

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient


# localhost 5000 -> host
# @app.route('/uri') => http://host + /uri


app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/reviews', methods=['POST'])
def init_review():
    delete = request.form['delete']
    client = MongoClient('localhost', 27017)
    if delete == 'OK':
        review_tbl = client.book_review_db.review
        review_tbl.delete_many({})

    result = {'result':'success','msg':'리뷰초기화'}
    return jsonify(result)

@app.route('/review', methods=['POST'])
def add_review():
    author = request.form['author']
    title = request.form['title'] # post로 보낼때는 받는 데이터 인자''를 얻어온다.
    bookReview = request.form['bookReview']
    review_data = {'author' : author, 'title' : title, 'bookReview' : bookReview }

    client = MongoClient('localhost', 27017)
    review_tbl = client.book_review_db.review

    review_tbl.insert_one(review_data)

    result = {'result':'success','msg':'리뷰등록완료'}
    return jsonify(result)

@app.route('/review', methods=['GET'])
def get_review():
    client = MongoClient('localhost', 27017)
    review_tbl = client.book_review_db.review
    review_list = list(review_tbl.find({},{'_id': False}))
    result = {'result' : 'success','msg' : review_list}
    # { 'result' : 'success', 'msg' = review_list }
    return jsonify(result)

if __name__ == '__main__':
    app.run()
