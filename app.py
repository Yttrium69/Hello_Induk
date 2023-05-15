from flask import Flask, render_template, jsonify
import json

app=Flask(__name__)
app.config['JSON_AS_ASCII'] = False

json_data=[
    {"딸기":"가 좋아"},
    {"당근":"도 좋아"}
]

@app.route('/')
def gogo_main():
    return render_template('main.html')

@app.route('/get_main_data', methods=["GET"])
def get_main_data():
    return jsonify(json_data)

@app.route('/main', methods=["GET"])
def show_main_page():
    return render_template('main.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)