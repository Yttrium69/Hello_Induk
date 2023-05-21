$(document).ready(function () {
    get_json_and_do("/get_best_item_json", fill_best_items);
    get_json_and_do("/get_time_item_json", fill_time_items);
    write_left_time();
    get_json_and_do(`/get_category_item?category=A`, fill_category_items);
    gogo_nav();
    auto_slide();
})

function auto_slide(){
    setInterval(slide, 3000);
}

function slide() {
    var all_slide = $(".slide_item");
    var now_idx = 0;

    all_slide.each(function (idx, item) {
        $(this).hide();
        if ($(this).hasClass("active")) {
            now_idx = idx;
        }
    })

    let new_idx = 0;
    if (now_idx === all_slide.length - 1) {
        new_idx = 0;
    }
    else {
        new_idx = now_idx + 1;
    }

    all_slide.each(function () {
        $(this).removeClass("active");
    })

    all_slide.eq(new_idx).addClass("active");
    all_slide.eq(new_idx).show();
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

function pressed_category_tag(selected_tag){
    const tag_list=$(".tag_list li");
    for(let i=0;i<tag_list.length;i++){
        tag_list[i].style.backgroundColor="#EBEBEB";
        tag_list[i].style.color="#333333";
        tag_list.eq(i).removeClass("checked");
    }
    selected_tag.style.backgroundColor="#0085FF";
    selected_tag.style.color="white";
    $(selected_tag).addClass("checked");

    get_json_and_do(`/get_category_item?category=${selected_tag.getAttribute('name')}`,fill_category_items);
    $(".category_section button").html(`${selected_tag.innerHTML} 상품 더보기 >`)
}

function fill_category_items(items){
    const container=$(".category_section .item_container");
    container.empty();
    const json_data=JSON.parse(items)
    for(let i=0;i<json_data.length;i++){
        let json_item = json_data[i];
        let item_card=new_item_card_of(json_item);
        container.append(item_card);
    }

    const tags_of_category_section=$(".category_section .tag");
    for(let i=0;i<tags_of_category_section.length;i++){
        tags_of_category_section.eq(i).addClass("hide")
    }
}

function gogo_category(){
    const checked=$(".checked");
    location.href=`/category_item?category=${checked.attr("name")}`;
}