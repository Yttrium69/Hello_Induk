$(document).ready(function () {
    gogo_nav();
})

function get_final_price(){
    const base_price=$(".price").data("price");
    const option_cards=$(".option");

    let final_price=base_price;

    for(let i=0;i<option_cards.length;i++){
        if(option_cards.eq(i).hasClass("hide")){}
        else{
            const option_price=parseInt(option_cards.eq(i).data("option_price"));
            final_price+=option_price;
        }
    }
    return final_price+"원";
}

function update_final_price(){
    const pannel=$(".final_price");
    pannel.text(get_final_price());
}

function append_option_card(event_obj){
    const option_title=event_obj.target.value;
    const option_cards=$(".option")

    for(let i=0;i<option_cards.length;i++){
        const card_title=option_cards.eq(i).data("option_title");
        if(card_title==option_title){
            option_cards.eq(i).removeClass("hide");
        }
    }

    update_final_price();
}

function get_option_title_selected(){
    const option_cards=$(".option")
    let title_list=[];
    for(let i=0;i<option_cards.length;i++){
        if(option_cards.eq(i).hasClass("hide")){}
        else{
            title_list.push(option_cards.eq(i).data("option_title"));
        }
    }
    return title_list;
}

function submit_buy(){
    const item_id=$(".item_detail").data("item_id");
    const option_title_list=get_option_title_selected();
    const price=$(".final_price").text();
    const today=new Date();
    const bought_time=`${today.getFullYear()}년 ${today.getMonth()+1}월 ${today.getDate()}일 ${today.getHours()}:${today.getMinutes()}:${today.getSeconds()}`;

    
    // var user_id = sessionStorage.getItem('user_id');
    // console.log(user_id);

    const new_json={
        "item_id":item_id,
        "option_title_list":option_title_list,
        "price":price,
        "bought_time": bought_time,
    }

    fetch('/item_detail', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(new_json)
      }).then(function(request){
        return request.json();}
      ).then(function(json_data){
        alert(json_data.message);
      })
}

function delete_option(target){
    target=$(target).parent();
    target.addClass("hide");
    update_final_price();
}