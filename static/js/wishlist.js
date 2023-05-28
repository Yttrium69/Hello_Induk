$(document).ready(function(){
    nav_gogo();
})
function pressed_x_btn(target){
    fetch( `/delete_in_wishlist?item_id=${$(target).parent().parent().data("item_id")}`).
    then(function(response){
        return response.json();
    }).
    then(function(json_data){
        console.log(json_data.message)
        alert(json_data.message)
    }).
    then(function(){
        location.reload()
    })

}