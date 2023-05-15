$(document).ready(function () {
    console.log("gogo")
    get_best_json();


})

function click_slide(idx) {
    const banner = document.querySelector(".banner_img img");
    const slider_icon_arr = document.querySelectorAll(".slider_item img")
    const banner_div = document.querySelector(".banner_img")

    banner.src = `../img/banner/banner_${idx}.png`
    for (let i = 0; i < slider_icon_arr.length; i++) {
        slider_icon_arr[i].src = "../img/icon/icon_slider_false.svg";
    }
    slider_icon_arr[idx].src = "../img/icon/icon_slider_true.svg";
}

function auto_slide() {
    $(".slide_item").hide();
    var all_slide = $(".slide_item");
    var all_controller = $(".slider_item img");

    var now_idx = 0;

    all_slide.each(function (idx, item) {
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

    all_controller.each(function () {
        $(this).attr("src", "../img/icon/icon_slider_false.svg");
    });

    all_controller.eq(new_idx).attr("src", "../img/icon/icon_slider_true.svg");

}

function get_best_json() {
    let res = "GOGO";
    $.ajax({
        type: 'GET',
        url: 'http://127.0.0.1:5000/get_best_data',
        dataType: 'JSON',
        success: function (result) {
            for (let i = 0; i < result.length; i++) {
                let json_item = result[i];
                const new_card = create_item_card_of(json_item);
                const card_list_container = $(".comp_product_list");
                card_list_container.append(new_card);
            }
        },
        error: function (xtr, status, error) {
            // alert(xtr +":"+status+":"+error);
        }
    })
}

function create_item_card_of(elem) {
    const idx=elem['idx'];
    const title = elem['title'];
    let price = elem['price'];
    const discount = elem['discount'];
    price = price - price * (parseInt(discount) / 100);

    let discount_span;

    if (discount != 0) {
        discount_span = `<span style="display: inline-block;"class="discount_text  font_700">${discount}%</span>`;
    }
    else {
        discount_span = `<span></span>`;
    }

    const new_card = $(`<div class="comp_item-card">
        <div class="product_img_container">
            <img src="../static/img/product/A00000001.png">
        </div>
        <div class="comp_like">
            <img src="../static/img/icon/icon_heart_false.svg">
        </div>
        <div class="product_item_text">
            <p class="font_B5B5B5_12">추천 상품</p>
            <p class="font_333333_16">${title}</p>
            <div class="item-card_price">
            ${discount_span}
                <p style="display: inline-block;" class="price_next_discount  font_700">${price}원</p>
            </div>
        </div>
        </div>`);
    if(idx<4){
        new_card.addClass("show");
    }
    else{
        new_card.hide();
    }
    return new_card;
}


function slide_next() {
    let item_cards = $(".comp_item-card");
    let idx_shown_idx = 0;
    let idx = 0;

    item_cards.each(function () {
        $(this).hide();
    })
    for (let i = 0; i < item_cards.length; i++){
        if (item_cards.eq(i).hasClass("show")) {
            idx_shown_idx = i;
            break;
        }
    }

    if (idx_shown_idx === item_cards.length - 1) {
        idx_shown_idx = 0;
    }

    let idx_to_show = parseInt((idx_shown_idx  + 4) / 4);
    if(parseInt(item_cards.length/4)==idx_to_show) idx_to_show=0;

    for (let i = 0; i < item_cards.length; i++){
        item_cards.eq(i).removeClass("show");
    }

    for (let i = 0; i < item_cards.length; i++) {
        if (parseInt(i / 4) === idx_to_show) {
            item_cards.eq(i).addClass("show");
        }
    }

    for (let i = 0; i < item_cards.length; i++){
        if(item_cards.eq(i).hasClass("show"))item_cards.eq(i).show();
    }
}

function slide_prev(){
    let item_cards = $(".comp_item-card");
    let idx_shown_idx = 0;
    let idx = 0;

    item_cards.each(function () {
        $(this).hide();
    })
    for (let i = 0; i < item_cards.length; i++){
        if (item_cards.eq(i).hasClass("show")) {
            idx_shown_idx = i;
            break;
        }
    }

    if (idx_shown_idx === 0) {
        idx_shown_idx = item_cards.length;
    }

    let idx_to_show = parseInt((idx_shown_idx  - 4) / 4);
    // if(parseInt(item_cards.length/4)==idx_to_show) idx_to_show=0;

    for (let i = 0; i < item_cards.length; i++){
        item_cards.eq(i).removeClass("show");
    }

    for (let i = 0; i < item_cards.length; i++) {
        if (parseInt(i / 4) === idx_to_show) {
            item_cards.eq(i).addClass("show");
        }
    }

    for (let i = 0; i < item_cards.length; i++){
        if(item_cards.eq(i).hasClass("show"))item_cards.eq(i).show();
    }
}

