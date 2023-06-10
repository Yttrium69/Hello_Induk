import os
from flask import Flask, render_template, jsonify, redirect, url_for
from flask import request
from flask import session
from data_models import User, Item, db, Option, Post, Order, Wishlist, Board, Comment
import datetime
from sqlalchemy import desc

now_dir=os.path.abspath(os.path.dirname(__file__))

app=Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+f'{now_dir}/instance/models.db'
app.secret_key = 'super secret key'

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

def get_post_data(id):
    items=db.session.query(Post).all()
    for item in items:
        if(item.item_id==id):
            return item
    return {"id":"X000000", "name":"error"}

def get_option_data_list(id):
    items=db.session.query(Option).filter(Option.item_id==id).all()
    return items



@app.route('/db/Item')
def show_product_db():
    res_all=db.session.query(Item).all()
    res_str=""
    for res in res_all:
        res_str+=f'{res.id}>> item_id: {res.item_id} name:{res.name} price:{res.price} discount:{res.discount}</br>'
    return res_str

@app.route('/db/Option')
def show_option_db():
    res_all=db.session.query(Option).all()
    res_str=""
    for res in res_all:
        res_str+=f'{res.id}>> item_id: {res.item_id} option_title:{res.option_title} option_price:{res.option_price}</br>'
    return res_str

@app.route('/db/Post')
def show_post_db():
    res_all=db.session.query(Post).all()
    res_str=""
    for res in res_all:
        res_str+=f'{res.id}>></br>  item_id: {res.item_id}</br>  capacity:{res.capacity}</br> caution:{res.caution}</br> discription:{res.discription}</br> </br> </br> '
    return res_str

@app.route('/db/User')
def show_user_db():
    res_all=db.session.query(User).all()
    res_str=""
    for res in res_all:
        res_str+=f'{res.id}>></br>  user_id: {res.user_id}</br>  user_pw:{res.user_pw}</br> user_name:{res.user_name}</br></br></br></br> '
    return res_str

@app.route('/db/Order')
def show_order_db():
    res_all=db.session.query(Order).all()
    res_str=""
    for res in res_all:
        res_str+=f'{res.id}>></br>  order_id: {res.order_id}</br>  status:{res.status}</br> item_id:{res.item_id}</br>time:{res.time}</br>count:{res.count}</br>option_list:{res.option_list}</br>user_id:{res.user_id}</br></br></br></br> '
    return res_str


@app.route('/show_db')
def show_db():
    db_category=request.args.get("category", "Item")
    db_all=None
    if(db_category=="Item"): 
        db_all=db.session.query(Item).all()
    elif(db_category=="User"): 
        db_all=db.session.query(User).all()
    elif(db_category=="Option"): 
        db_all=db.session.query(Option).all()
    elif(db_category=="Post"): 
        db_all=db.session.query(Post).all()
    elif(db_category=="Order"): 
        db_all=db.session.query(Order).all()
    elif(db_category=="Wishlist"): 
        db_all=db.session.query(Wishlist).all()
    elif(db_category=="Board"): 
        db_all=db.session.query(Board).all()
    elif(db_category=="Comment"): 
        db_all=db.session.query(Comment).all()

    # items = [item.__dict__ for item in db_all]

    return render_template("show_db.html", item=db_all)

        
@app.route('/')
def gogo_main():
    board_data=db.session.query(Board).order_by(desc(Board.id)).all()[:4]
    return render_template('index.html', Wishlist=Wishlist, boards = board_data)

@app.route('/get_best_item_json', methods=["GET"])
def get_best_item_data():
    best_id_list=["D000000", "A000002", "A000003", "A000004", "A000005", "C000000", "A000006", "C000001", "C000002", "B000000", "E000000", "A000007"]
    best_item_list=[]
    for id in best_id_list:
        item=get_item_data(id)
        new_json={"id": item.item_id, "name":item.name, "price":item.price, "discount":item.discount}
        best_item_list.append(new_json)
    return jsonify(best_item_list)

@app.route('/get_time_item_json', methods=["GET"])
def get_time_item_data():
    time_id_list=["B000000", "C000000"]
    time_item_list=[]

    for id in time_id_list:
        item=get_item_data(id)
        new_json={"id": item.item_id, "name":item.name, "price":item.price, "discount":item.discount}
        time_item_list.append(new_json)

    return jsonify(time_item_list)

@app.route('/is_in_wish_list')
def is_in_wish_list():
    item_id=request.args.get('item_id')
    is_in=None
    if(db.session.query(Wishlist).filter(Wishlist.item_id==item_id, Wishlist.user_id==session.get('user_id')).first()==None):
        is_in=False
    else:
        is_in=True
    
    return jsonify({"result":is_in})

def get_category_name(category_id):
    if(category_id=="A"):
        return "인형"
    elif(category_id=="B"):
        return "돕바/과잠"
    elif(category_id=="C"):
        return "포스터"
    elif(category_id=="D"):
        return "텀블러/컵/문구류"
    elif(category_id=="E"):
        return "모자"
    else:
        return "카테고리 없음"
    
def new_order_id():
    id_list=db.session.query(Order).all()
    if(len(id_list)==0):
        return "0000000"
    last_id = id_list[len(id_list)-1].order_id

    new_id=str('{:08d}'.format(int(last_id)+1))
    return new_id


@app.route('/item_detail', methods=['GET', 'POST'])
def item_detail():
    if(request.method=="GET"):
        id=request.args.get('id', "X000000")
        if(id=="X000000"):
            return "상품 페이지를 찾을 수 업습니다."

        item_data=get_item_data(id)
        post_data=get_post_data(id)
        option_list=get_option_data_list(id)

        print(item_data.name)
        print(post_data)
        print(option_list)

        return render_template('item_detail.html',
            item=item_data,
            item_id=id,
            category_name=get_category_name(id[0]),
            item_name=item_data.name,
            discription=post_data.discription,
            price=item_data.price,
            capacity=post_data.capacity,
            caution=post_data.caution,
            option_list=option_list,
            wishlist_db=db.session.query(Wishlist).filter(Wishlist.user_id==session.get('user_id')),
            Wishlist=Wishlist)
    
    elif(request.method=="POST"):
        if(session.get('user_id')==None):
            return jsonify({"message":"로그인 후 이용하세요."})
        
        order_data=request.json
        print(order_data)
        user_id=session['user_id']
        order_id=new_order_id()
        time=order_data['bought_time']
        item_id=order_data['item_id']
        option_list=order_data['option_title_list']
        option_str=""

        for option in option_list:
            option_str+=str(option)+"&"
        
        if(len(option_str)!=0):
            option_str=option_str[:-1]

        append_order_list(item_id=item_id, order_id=order_id, time=time, user_id=user_id, option_list=option_str)

        return jsonify({"message":"주문이 완료되었습니다."})

@app.route('/category_item', methods=['GET'])
def category_item():
    category=request.args.get("category", "추천상품")
    items=None
    if(category=="추천상품" or category=="신상품"):
        items=db.session.query(Item).all()
        return render_template("category_item.html", category=category,items=items, Wishlist=Wishlist, wishlist_db=db.session.query(Wishlist))
    items=db.session.query(Item).filter(Item.item_id.like(category+"%")).all()
    return render_template("category_item.html",Wishlist=Wishlist, wishlist_db=db.session.query(Wishlist),category=get_category_name(category),items=items)

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
            return ("<script>location.href='/'</script>")
    
        return render_template("signin.html", span="아이디와 비밀번호가 일치하지 않습니다.")
    
@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for("gogo_main"))

@app.route('/adminpage', methods=['GET'])
def adminpage():
    return render_template("adminpage.html")

def new_item_id_of(category):
    id_list=db.session.query(Item).filter(Item.item_id.like(category+"%")).all()
    print(len(id_list))
    if(len(id_list)==0):
        return category +"000000"
    last_id = id_list[-1].item_id
    last_number = int(last_id[len(category):])  # Extract the numeric part of the last ID
    new_number = last_number + 1
    new_id = category + '{:06d}'.format(new_number)
    return new_id

def append_item(id, name, price, discount):
    new_item=Item(id=id, name=name, price=price, discount=discount)

    db.session.add(new_item)
    db.session.commit()

def append_option(item_id,option_id, title, price):
    new_option=Option(item_id=item_id, option_id=option_id, option_title=title, option_price=price)
    db.session.add(new_option)
    db.session.commit()

def append_post(item_id, capacity, caution, discription):
    new_post=Post(item_id=item_id, capacity=capacity, caution=caution, discription=discription)
    db.session.add(new_post)
    db.session.commit()

def append_order_list(order_id, item_id, time,user_id,  option_list="", status="주문 확인", count=1):
    new_order=Order(order_id=order_id, item_id=item_id, time=time, option_list=option_list,user_id=user_id, count=count,status=status)
    db.session.add(new_order)
    db.session.commit()


@app.route('/admin_upload_item', methods=['GET', 'POST'])
def admin_upload_item():
    if(request.method=='GET'):
        return render_template("admin_upload_item.html")
    elif(request.method=='POST'):
        category_selected = request.form['category_selected']
        item_id=new_item_id_of(category_selected)
        name = request.form['name']
        price = request.form['price']
        discount = request.form['discount']
        option_name_arr=request.form.getlist('option_name')
        option_price_arr=request.form.getlist('option_price')
        detail_img_arr=request.files.getlist('detail_img')
        rep_img=request.files['rep_img']
        capacity=request.form['capacity']
        caution=request.form['caution']
        discription=request.form.get('discription')

        detail_cnt=0
        for img in detail_img_arr:
            img.save(f'static/img/detail/{item_id}_{str(detail_cnt)}.png')
            detail_cnt+=1

        rep_img.save(f'static/img/item/{item_id}.png')

        append_item(id=item_id, name=name, price=price, discount=discount)

        for i in range(len(option_name_arr)):
            option_name=option_name_arr[i]
            option_price=option_price_arr[i]

            append_option(item_id=item_id,option_id=f'{item_id}_{i}', price=option_price, title=option_name)

        append_post(item_id=item_id, capacity=capacity, caution=caution, discription=discription)

        return redirect(url_for("admin_upload_item"))


    return redirect(url_for("gogo_main"))

@app.route('/wishlist', methods=['GET'])
def wishlist():
    wishes=db.session.query(Wishlist).filter(Wishlist.user_id==session.get('user_id')).all()
    item_list=[]
    for wish in wishes:
        item_id=wish.item_id
        item_list.append(db.session.query(Item).filter(Item.item_id==item_id).first())

    return render_template("wishlist.html", items=item_list)
    
@app.route('/add_wish_list', methods=['GET'])
def add_wish_list():
    item_id=request.args.get("item_id")
    new_json=None
    if(session.get('user_id') is None):
        new_json={"result":"false", "message":"로그인 후 이용하세요."}
        print(new_json)
        print(jsonify(new_json))
        return jsonify(new_json)
    if(db.session.query(Wishlist).filter(Wishlist.user_id==session.get('user_id'), Wishlist.item_id==item_id).first()!=None):
        return jsonify({"result":"true", "message":"이미 장바구니에 있는 상품입니다."})
    new_wish=Wishlist(user_id=session.get('user_id'), item_id=item_id)
    db.session.add(new_wish)
    db.session.commit()
    return jsonify({"result":"true", "message":"장바구니에 추가되었습니다."})

@app.route('/delete_in_wishlist')
def delete_in_wishlist():
    item_id_to_delete=request.args.get('item_id')
    db.session.query(Wishlist).filter(Wishlist.user_id==session.get('user_id'), Wishlist.item_id==item_id_to_delete).delete()
    db.session.commit()
    return jsonify({"message":"상품이 삭제되었습니다."})


@app.route('/admin_sold_list')
def sold_list():
    return render_template("admin_sold_list.html", item=db.session.query(Order).all())


@app.route('/board')
def board():
    post_list = db.session.query(Board).order_by(desc(Board.id)).all()
    return render_template("board.html", items = post_list)

@app.route('/write_board', methods=['GET', 'POST'])
def write_board():
    if request.method=='GET':
        return render_template("write_board.html")
    elif request.method == 'POST':
        writer_id = str(session['user_id'])
        title = request.form['post_title']
        content = request.form['post_content']
        date = str(datetime.date.today())

        new_post = Board(writer_id = writer_id, title = title, content = content, data = date)

        db.session.add(new_post)
        db.session.commit()

        post_id = db.session.query(Board).order_by(desc(Board.id)).first().id

        return (f'<script>alert("게시글이 등록되었습니다."); location.href="/user_post?post_id={post_id}"</script>')
    
@app.route('/user_post', methods=['GET', 'POST'])
def user_post():
    if request.method == "GET":
        post_id =  request.args.get("post_id")
        post = db.session.query(Board).filter(Board.id == post_id).first()
        comment_list = db.session.query(Comment).filter(Comment.post_id == post_id).all()
        return render_template("user_post.html", post_item = post, comment_items = comment_list)
    
@app.route('/write_comment', methods = ['POST'])
def write_comment():
    if request.method == "POST":
        post_id = request.args.get("post_id")
        comment = request.form.get("comment_content")
        commenter_id = session['user_id']
        data = str(datetime.date.today())
        
        new_comment = Comment(post_id = post_id, content = comment, commenter_id = commenter_id, data = data)

        db.session.add(new_comment)
        db.session.commit()

        return (f'<script>alert("댓글이 등록되었습니다."); location.href="/user_post?post_id={post_id}"</script>')
    

@app.route('/delete_post', methods = ['GET'])
def delete_post():
    post_id = request.args.get("post_id")
    post_to_delete = db.session.query(Board).filter(Board.id == post_id).first()
    comments_of_post = db.session.query(Comment).filter(Comment.post_id == post_id).all()

    for comment in comments_of_post:
        db.session.delete(comment)

    db.session.delete(post_to_delete)
    db.session.commit()
    
    return (f'<script>alert("게시글이 삭제되었습니다."); location.href="/board"</script>')

@app.route('/update_post', methods = ['GET', 'POST'])
def update_post():
    if request.method == "GET":
        post_id = request.args.get("post_id")
        post_to_update = db.session.query(Board).filter(Board.id == post_id).first()
        return render_template("update_post.html", post = post_to_update)
    elif request.method == "POST":
        post_id = request.form.get("post_id")

        post_to_update = db.session.query(Board).filter(Board.id == post_id).first()

        post_to_update.content = request.form.get("post_content")
        post_to_update.title = request.form.get("post_title")
        post_to_update.data = str(datetime.date.today())

        db.session.commit()

        return (f'<script>alert("게시글이 수정되었습니다.");location.href="/user_post?post_id={post_id}"</script>')


if __name__ == '__main__':
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(host='0.0.0.0', port=5000, debug=False)
