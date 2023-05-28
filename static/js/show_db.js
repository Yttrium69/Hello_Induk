$(document).ready(function(){
    gogo_nav();
})

function change_db(event_obj){
    const db_category=event_obj.target.value;
    location.href=`/show_db?category=${db_category}`;
}