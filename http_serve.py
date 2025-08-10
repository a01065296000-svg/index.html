from flask import Flask, request, jsonify

app = Flask(__name__)

memory = {}

@app.route('/')
def home():
    return "안녕하세요, Aceto HTTP 서버에 오신 것을 환영합니다!"

@app.route('/memory', methods=['GET', 'POST'])
def memory_handler():
    if request.method == 'POST':
        data = request.json
        key = data.get('key')
        value = data.get('value')
        memory[key] = value
        return jsonify({"message": f"{key} 저장 완료", "memory": memory})
    else:
        return jsonify(memory)

if __name__ == '__main__':
    app.run(debug=True)