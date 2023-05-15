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

@app.route('/get_best_data', methods=["GET"])
def get_best_data():
    best_json=[
        {"idx":"0", "title":"과즙 팡팡! 인덕이 젤리0", "discount":"50", "price":"6400"},
        {"idx":"1", "title":"과즙 팡팡! 인덕이 젤리1", "discount":"10", "price":"6400"},
        {"idx":"2", "title":"과즙 팡팡! 인덕이 젤리2", "discount":"0", "price":"6400"},
        {"idx":"3", "title":"과즙 팡팡! 인덕이 젤리3", "discount":"100", "price":"6400"},
        {"idx":"4", "title":"과즙 팡팡! 인덕이 젤리4", "discount":"50", "price":"6400"},
        {"idx":"5", "title":"과즙 팡팡! 인덕이 젤리5", "discount":"0", "price":"6400"},
        {"idx":"6", "title":"과즙 팡팡! 인덕이 젤리6", "discount":"30", "price":"6400"},
        {"idx":"7", "title":"과즙 팡팡! 인덕이 젤리7", "discount":"70", "price":"6400"},
        {"idx":"8", "title":"과즙 팡팡! 인덕이 젤리8", "discount":"50", "price":"6400"},
        {"idx":"9", "title":"과즙 팡팡! 인덕이 젤리9", "discount":"0", "price":"6400"},
        {"idx":"10", "title":"과즙 팡팡! 인덕이 젤리10", "discount":"30", "price":"6400"},
        {"idx":"11", "title":"과즙 팡팡! 인덕이 젤리11", "discount":"70", "price":"6400"},
    ]
    return jsonify(best_json)

@app.route('/main', methods=["GET"])
def show_main_page():
    return render_template('main.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)