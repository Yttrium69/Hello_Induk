import os
from flask import Flask, render_template, jsonify, redirect, url_for
from flask import request
from flask import session
from data_models import User, Item, db

now_dir=os.path.abspath(os.path.dirname(__file__))

app=Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+f'{now_dir}/instance/models.db'

db.init_app(app)
db.app=app

with app.app_context():
    db.create_all()


def get_item_data(id):
    items=db.session.query(Item).all()
    for item in items:
        if(item.item_id==id):
            return item
    return {"id":"X000000", "name":"error"}



@app.route('/db/Item')
def show_product_db():
    res_all=db.session.query(Item).all()
    res_str=""
    for res in res_all:
        res_str+=f'{res.id}>> item_id: {res.item_id} name:{res.name} price:{res.price} discount:{res.discount}</br>'
        print(res_str)
    return res_str
        
@app.route('/')
def gogo_main():
    return render_template('main.html')

@app.route('/get_best_item_json', methods=["GET"])

def get_best_item_data():
    best_id_list=["A000006", "B000008", "A000011", "A000013", "A000009", "B000010", "D000001", "C000007", "C000013", "D000002", "D000004", "D000005"]
    best_item_list=[]
    for id in best_id_list:
        item=get_item_data(id)
        new_json={"id": item.item_id, "name":item.name, "price":item.price, "discount":item.discount}
        best_item_list.append(new_json)
    return jsonify(best_item_list)

@app.route('/get_time_item_json', methods=["GET"])
def get_time_item_data():
    time_id_list=["C000013", "D000002"]
    time_item_list=[]

    for id in time_id_list:
        item=get_item_data(id)
        new_json={"id": item.item_id, "name":item.name, "price":item.price, "discount":item.discount}
        time_item_list.append(new_json)

    return jsonify(time_item_list)

@app.route('/item_detail', methods=['GET'])
def get_time_item_json():
    id=request.args.get('id', "X000000")
    if(id=="X000000"):
        return "상품 페이지를 찾을 수 업습니다."
    
    item=get_item_data(id)
    return render_template('item_detail.html', item_json=item.name)

@app.route('/category_item', methods=['GET'])
def category_item():
    category=request.args.get("category", "X")
    return render_template("category_item.html", category=category)

@app.route('/get_category_item', methods=["GET"])
def get_category_item():
    category=request.args.get("category")
    item_arr=db.session.query(Item).all()
    res_arr=[]
    i=0
    for item in item_arr:
        if(i==20):
            break
        if(item.item_id[0]==category):
            res_arr.append({"id": item.item_id, "name":item.name, "price":item.price, "discount":item.discount})
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
        id=request.form['user_id']
        pw=request.form['user_pw']
        name=request.form['user_name']
        new_user=User(user_id=id, user_name=name, user_pw=pw)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for(f'signup_succeed', name=name))
    
@app.route('/signup_succeed', methods=['GET'])
def signup_succeed():
    return render_template("signup_succeed.html", name=request.args.get("name"))
    
@app.route('/signup_same_id_NONO', methods=['POST'])
def signup_same_id_NONO():
    id=request.json['user_id']
    if(db.session.query(User).filter(User.user_id==id).first()!=None):
        return {"sameNONO":False}
    return({"sameNONO":True})

@app.route('/signup_same_name_NONO', methods=['POST'])
def signup_same_name_NONO():
    name=request.json['user_name']
    if(db.session.query(User).filter(User.user_name==name).first()!=None):
        return {"sameNONO":False}
    return({"sameNONO":True})


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if(request.method=="GET"):
        return render_template("signin.html")
    elif(request.method=="POST"):
        id=request.form['user_id']
        pw=request.form['user_pw']
    
        if(db.session.query(User).filter(User.user_id==id, User.user_pw==pw).first()!=None):
            session['user_id']=id
            return redirect(url_for("gogo_main"))
    
        return render_template("signin.html", span="아이디와 비밀번호가 일치하지 않습니다.")
    
@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for("gogo_main"))

@app.route('/adminpage', methods=['GET'])
def adminpage():
    return render_template("adminpage.html")

@app.route('/admin_upload_item', methods=['GET'])
def admin_upload_item():
    if(request.method==['GET']):
        return render_template("admin_upload_item.html")
    return render_template("admin_upload_item.html")




if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(host='127.0.0.1', port=5000, debug=True)