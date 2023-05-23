from flask import Flask, render_template, jsonify
from flask import request

import json

app=Flask(__name__)
app.config['JSON_AS_ASCII'] = False

item_json=[
    {"idx":"6", "id":"A000006", "name":"너무 귀여워! 핑크베어", "price":12000,"discount":50, "option_id_arr":["A000006-0"]},
    {"idx":"9", "id":"A000009", "name":"안뇽이랑 색깔친구 파랑파랑", "price":15000,"discount":0,"option_id_arr":[]},
    {"idx":"11", "id":"A000011", "name":"계란후라이가 좋은 안뇽이 친구", "price":10000,"discount":10,"option_id_arr":[]},
    {"idx":"13", "id":"A000013", "name":"옆으로 아장아장 꽃게인형", "price":3000,"discount":0,"option_id_arr":["A000013-0, A000013-1, A000013-2"]},
    {"idx":"14", "id":"A000014", "name":"처음처럼 부드러워 근본 진로", "price":50000,"discount":30,"option_id_arr":[]},
    {"idx":"8", "id":"B000008", "name":"인하대학교 한문 돕바 Black", "price":70000,"discount":10,"option_id_arr":[]},
    {"idx":"10", "id":"B000010", "name":"인하대학교 한문 돕바 White", "price":70000,"discount":10,"option_id_arr":[]},
    {"idx":"7", "id":"C000007", "name":"안뇽인덕 포스터 기본", "price":8000,"discount":0,"option_id_arr":[]},
    {"idx":"13", "id":"C000013", "name":"안뇽인덕 잔디 포스터", "price":10000,"discount":0,"option_id_arr":[]},
    {"idx":"1", "id":"D000001", "name":"헬로 안녕 에어팟 키링", "price":12000,"discount":10,"option_id_arr":[]},
    {"idx":"2", "id":"D000002", "name":"둥글둥글 귀여워! 겸둥 카메라 모형 set", "price":36000,"discount":10,"option_id_arr":["D000002-0", "D000002-1", "D000002-2"]},
    {"idx":"3", "id":"D000003", "name":"파스텔 컬러 연습장 4종", "price":1500,"discount":0,"option_id_arr":["D000003-0","D000003-1","D000003-2", "D000003-3"]},
    {"idx":"4", "id":"D000004", "name":"즐거운 일은 매일 있어 화이트 연습장", "price":1300,"discount":00,"option_id_arr":[]},
    {"idx":"5", "id":"D000005", "name":"사각사각 반투명 메모지", "price":1000,"discount":0,"option_id_arr":[]},
]
error_item=[{"id":"X000000", "name":"error"}]
best_json=[
    {"idx":"0", "id":"A000011", "name":"계란후라이가 좋은 안뇽이 친구", "price":10000,"discount":10,"option_id_arr":[]},
    {"idx":"1", "id":"A000013", "name":"옆으로 아장아장 꽃게인형", "price":3000,"discount":0,"option_id_arr":["A000013-0, A000013-1, A000013-2"]},
    {"idx":"2", "id":"A000014", "name":"처음처럼 부드러워 근본 진로", "price":50000,"discount":30,"option_id_arr":[]},
    {"idx":"3", "id":"B000008", "name":"인하대학교 한문 돕바 Black", "price":70000,"discount":10,"option_id_arr":[]},
    {"idx":"4", "id":"B000010", "name":"인하대학교 한문 돕바 White", "price":70000,"discount":10,"option_id_arr":[]},
    {"idx":"5", "id":"C000007", "name":"안뇽인덕 포스터 기본", "price":8000,"discount":0,"option_id_arr":[]},
    {"idx":"6", "id":"C000013", "name":"안뇽인덕 잔디 포스터", "price":10000,"discount":0,"option_id_arr":[]},
    {"idx":"7", "id":"D000001", "name":"헬로 안녕 에어팟 키링", "price":12000,"discount":10,"option_id_arr":[]},
    {"idx":"8", "id":"D000002", "name":"둥글둥글 귀여워! 겸둥 카메라 모형 set", "price":36000,"discount":10,"option_id_arr":["D000002-0", "D000002-1", "D000002-2"]},
    {"idx":"9", "id":"D000003", "name":"파스텔 컬러 연습장 4종", "price":1500,"discount":0,"option_id_arr":["D000003-0","D000003-1","D000003-2", "D000003-3"]},
    {"idx":"10", "id":"D000004", "name":"즐거운 일은 매일 있어 화이트 연습장", "price":1300,"discount":00,"option_id_arr":[]},
    {"idx":"11", "id":"D000005", "name":"사각사각 반투명 메모지", "price":1000,"discount":0,"option_id_arr":[]},
]
time_json=[
    {"idx":"14", "id":"A000014", "name":"처음처럼 부드러워 근본 진로", "price":50000,"discount":30,"option_id_arr":[]},
    {"idx":"8", "id":"B000008", "name":"인하대학교 한문 돕바 Black", "price":70000,"discount":10,"option_id_arr":[]},
]

user_json=[
    {"idx":"0", "user_id":"dmswldmsgp00", "user_pw":"fkshdldk12!", "user_name":"이트륨"},
    {"idx":"1", "user_id":"dmswldmfdfssgp00", "user_pw":"fkshdldk12!", "user_name":"이트륨"},
    {"idx":"2", "user_id":"dmswldmssdfdsfgp00", "user_pw":"fkshdldk12!", "user_name":"이트륨"}
]

def get_item_json(id):
    item_arr=item_json
    for i in range(len(item_arr)):
        if(item_arr[i]["id"]==id):
            return item_arr[i]
    return error_item
        
@app.route('/')
def gogo_main():
    return render_template('main.html')

@app.route('/get_best_item_json', methods=["GET"])
def get_best_item__data():
    return jsonify(best_json)

@app.route('/get_time_item_json', methods=["GET"])
def get_time_item__data():
    return jsonify(time_json)

@app.route('/item_detail', methods=['GET'])
def get_time_item_json():
    id=request.args.get('id', "X000000")
    if(id=="X000000"):
        return "상품 페이지를 찾을 수 업습니다."
    
    json_item=get_item_json(id)
    return render_template('item_detail.html', item_json=json_item["name"])

@app.route('/category_item', methods=['GET'])
def category_item():
    category=request.args.get("category", "X")
    return render_template("category_item.html", category=category)

@app.route('/get_category_item', methods=["GET"])
def get_category_item():
    category=request.args.get("category")
    item_arr=item_json
    res_arr=[]
    i=0
    for item in item_arr:
        if(i==20):
            break
        if(item["id"][0]==category):
            res_arr.append(item)
            i+=1
    return jsonify(res_arr)

@app.route('/notice', methods=["GET"])
def notice():
    return render_template("notice.html")

@app.route('/error', methods=['GET'])
def error():
    return render_template("error.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if(request.method=='GET'):
        return render_template('signup.html')
    elif(request.method=='POST'):
        id=request['user_id']
        pw=request['user_pw']
        name=request['user_name']
        new_user={"idx":len(user_json)-1,"user_id":id, "user_pw":pw,  "user_name":name}
        user_json.append(new_user)
        return render_template('signup_succeed.html', name=name)

@app.route('/signup_same_id_NONO', methods=['POST'])
def signup_same_id_NONO():
    data=request.json
    for target in user_json:
        if(target['user_id']==data['user_id']):
            return jsonify({"sameNONO":False})
    return({"sameNONO":True})

@app.route('/signup_same_name_NONO', methods=['POST'])
def signup_same_name_NONO():
    data=request.json
    for target in user_json:
        if(target['user_name']==data['user_name']):
            return jsonify({"sameNONO":False})
    return({"sameNONO":True})

@app.route('/submit_signup_form', methods=['POST'])
def submet_signup_form():
    data=request.form
    new_user={"idx":len(user_json), "user_name":data['user_name'], "user_id":data["user_id"], "user_pw":data["user_pw"]}
    user_json.append(new_user)
    return render_template("signup_succeed.html", name=user_json)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if(request.method=="GET"):
        return render_template("signin.html")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)