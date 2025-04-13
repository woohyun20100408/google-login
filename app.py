from flask import Flask, request, jsonify, render_template
import datetime

app = Flask(__name__)

saved_data = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    saved_data.append([email, password, str(datetime.datetime.now())])
    return "저장 완료"

@app.route('/load', methods=['GET'])
def load():
    return jsonify(saved_data)

if __name__ == '__main__':
    # 여기서 호스트와 포트를 0.0.0.0으로 설정
    app.run(host="0.0.0.0", port=5000)
