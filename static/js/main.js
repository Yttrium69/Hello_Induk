$(document).ready(function () {
    get_json_and_do("/get_best_item_json", fill_best_items);
    // fill_time_items();
    // fill_category_items();
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
}
