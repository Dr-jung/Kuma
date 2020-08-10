from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/sparta')
def sparta():
    return '스파르타 안녕'

@app.route('/data')
def data():
    data = {'title':'책 제목','comment':'잼나'}
    return jsonify(data)

@app.route('/get', methods=['GET'])
def get():
    title = request.args.get('title') # Get으로 request에서 넘어온 인자''를 얻어온다.
    review = request.args.get('review')
    result = {'result' : 'success', 'title' : title, 'review' : review }
    return jsonify(result)
    # Dictionary ' 를 jsonify를 해주면 ' > " 로 변경됨 (제이슨 규격이 쌍따움표이나 딕션너리를 만들때는 '를 사용)

@app.route('/post', methods=['POST'])
def post():
    title = request.form['title'] # post로 보낼때는 받는 데이터 인자''를 얻어온다.
    result = {'result' : 'success', 'title' : title }
    return jsonify(result)


## API 역할을 하는 부분
@app.route('/test', methods=['GET'])
def test_get():
    title_receive = request.args.get('title_give')
    print(title_receive)
    return jsonify({'result': 'success', 'msg': '이 요청은 GET!'})


if __name__ == '__main__':
    app.run()
