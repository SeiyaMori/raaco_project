from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/users/')
def index():
    print(request.args.get("name"))
    return jsonify("HELLO")


@app.errorhandler(404)
def not_found(e):
    msg = e
    return msg



if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8000)
