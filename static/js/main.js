$(document).ready(function () {
    get_json_and_do("/get_best_item_json", fill_best_items);
    get_json_and_do("/get_time_item_json", fill_time_items);
    write_left_time();
})

function get_json_and_do(url, callback){
    const request = new XMLHttpRequest(); 
    request.onreadystatechange=function(){
        if(request.readyState==4){
            if (request.status === 200) { // successfully
                callback(request.response); // we're calling our method
            }
        }
    }
    request.open('GET', url, 'true');
    request.send();
}

function fill_best_items(data){
    const json_data=JSON.parse(data);
    for (let i = 0; i < json_data.length; i++) {
        let json_item = json_data[i];
        let item_card=new_item_card_of(json_item);
        let container=$(".best_section .item_container");
        container.append(item_card);
    }

    const item_card_arr=$(".best_section .item_card");
    for (let i = 0; i < json_data.length; i++){
        item_card_arr.eq(i).addClass('hide');
    }
    for(let i=0;i<4;i++){
        item_card_arr.eq(i).addClass('show');
        item_card_arr.eq(i).removeClass('hide');
    }
}

function new_item_card_of(json_item){
    const id=json_item.id;
    const name=json_item.name;
    let price=json_item.price;
    const discount=json_item.discount;

    let discount_span=``;
    if(discount!=0){
        discount_span=`<span class="discount_span">${discount}%</span>`
        price=price-price*discount/100;
    }

    const new_card=$(
        `<div class="item_card" name=${id}>
            <span class="tag">Best</span>
            <img onclick=pressed_like(this) style="display: block;" class="icon_like" src="../static/img/icon/icon_heart_false.svg">
            <img onclick="location.href='/item_detail?id=${id}'" class="card_img" src="../static/img/item/${id}.png">
            <p class="color_B5B5B5 size_12">${get_category(id)}</p>
            <a href="/item_detail?id=${id}"><p class="item_title">${name}</p></a>
            ${discount_span}
            <p style="display: inline-block;" class="weight_700">${price}원</p> 
        </div>`
        );
    return new_card;
}

function slide_next(){
    const item_card_arr=$(".best_section .item_card");
    let show_idx;
    for(let i=0;i<item_card_arr.length;i++){
        if(item_card_arr.eq(i).hasClass('show')){
            show_idx=i;
            break;
        }
    }
    if(show_idx===item_card_arr.length-4) show_idx=-4;
    show_idx+=4;
    for(let i=0;i<item_card_arr.length;i++){
        item_card_arr.eq(i).removeClass('show');
        item_card_arr.eq(i).addClass('hide');
    }
    for(let i=show_idx;i<show_idx+4;i++){
        toggle_hide(item_card_arr.eq(i));
    }
}

function slide_prev(){
    const item_card_arr=$(".best_section .item_card");
    let show_idx;
    for(let i=0;i<item_card_arr.length;i++){
        if(item_card_arr.eq(i).hasClass('show')){
            show_idx=i;
            break;
        }
    }
    if(show_idx===0) show_idx=item_card_arr.length;
    show_idx-=4;
    for(let i=0;i<item_card_arr.length;i++){
        item_card_arr.eq(i).removeClass('show');
        item_card_arr.eq(i).addClass('hide');
    }
    for(let i=show_idx;i<show_idx+4;i++){
        toggle_hide(item_card_arr.eq(i));
    }
}

function fill_time_items(data){
    const json_data=JSON.parse(data);
    for (let i = 0; i < 2; i++) {
        let json_item = json_data[i];
        let item_card=new_item_card_of(json_item);
        let container=$(".time_section .item_container");
        container.prepend(item_card);
    }
}

function write_left_time(){
    setInterval(function(){
        let today=new Date();
        let hour=23-today.getHours();
        let min=59-today.getMinutes();
        let sec=60-today.getSeconds();

        if(hour<10) hour="0"+String(hour);
        if(min<10) min="0"+String(min);
        if(sec<10) sec="0"+String(sec);
        
        $(".left_time").html(`${hour}:${min}:${sec}`);
    }, 1000)
}