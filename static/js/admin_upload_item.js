$(document).ready(function(){
    show_now_input_length(".description textarea", ".description .text_length", 200);
    show_now_input_length(".warning textarea", ".warning .text_length", 200);
})

function pressed_category_tag(self){
    const target=$(self);
    const category=self.getAttribute("value");
    console.log(category);
    const tag_list=$(".tag_list li");
    for(let i=0;i<tag_list.length;i++){
        tag_list.eq(i).css("background-color", "#EBEBEB");
        tag_list.eq(i).css("color", "#333333");
    }
    target.css("background-color", "#0085FF");
    target.css("color", "#FFFFFF");

    $(document).ready($(".category_selected").attr("val", category));
}

function show_now_input_length(now_input_src, show_span_src, max_length){
    const now_input=$(`${now_input_src}`);
    const show_span=$(`${show_span_src}`);

    now_input.on("propertychange change keyup paste input", function(){
        const length=now_input.val().length;
        show_span[0].value=length+"/"+max_length;
        if(length==0){
            show_span.css("color","#333333");
        }
        else if(max_length<length){
            show_span.css("color","rgb(255, 8, 0)");
        }
        else{
            show_span.css("color", "rgb(0, 102, 255)");
        }
    });
}

function delete_parent(target){
    target=$(target.parentElement);
    target.remove();
}

function new_option_card(){
    const new_card=$(`
        <div style="margin-bottom:10px;" class="option_card">
            <img onclick="delete_parent(this)" src="../static/img/icon/icon_x.svg">
            <span>옵션명</span><input name="option_name"  type="text" placeholder="상품명을 입력하세요.">
            <span>가격</span><input name="option_price" type="text" placeholder="가격을 입력하세요.">
        </div>
    `);
    return new_card;
}

function append_option_card(){
    const card_container=$(".option_container");
    const new_card=new_option_card();
    card_container.prepend(new_card);
}


function replace_img(container_src, event_obj) {
    const img_container = $(container_src);
    const file_list = event_obj.target.files;

    if (file_list.length === 0) {
        console.log("No file selected.");
        return;
    }

    const reader = new FileReader();

    reader.onload = function () {
        const new_card = new_img_div(reader.result);
        new_card.attr("name", "rep_img");
        img_container.empty(); // Clear existing image(s) in the container
        img_container.append(new_card); // Append the new image card
    }

    reader.readAsDataURL(file_list[0]); // Read the file as data URL
}


function append_detail_img(container_src, event_obj){
    const img_container = $(container_src);
    img_container.empty();
    let file_list = event_obj.target.files;
    
    console.log(file_list.length)

    if (file_list.length === 0) {
        console.log("No file selected.");
        return;
    }

    for(let i=0;i<file_list.length;i++){
        const reader = new FileReader();

        reader.onload = function () {
            const new_card = new_img_div(reader.result);
            img_container.append(new_card);
        }

        reader.readAsDataURL(file_list[i]);
    }
}

function remove_me(target){
    $(target).remove();
}

function new_img_div(img_src) {
    const new_img_div = $("<img class='item_img' onclick='remove_me(this)' style='width:510px; object-fit: cover; height:auto;'/>").attr("src", img_src);

    return new_img_div;
}