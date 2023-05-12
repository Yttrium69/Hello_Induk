
$(document).ready(function(){
    console.log("gogo")
    $(".slide_item").hide();
    setInterval(auto_slide, 4000);
})

function click_slide(idx){
    const banner=document.querySelector(".banner_img img");
    const slider_icon_arr=document.querySelectorAll(".slider_item img")
    const banner_div=document.querySelector(".banner_img")

    banner.src=`../img/banner/banner_${idx}.png`
    for(let i=0;i<slider_icon_arr.length;i++){
        slider_icon_arr[i].src="../img/icon/icon_slider_false.svg";
    }
    slider_icon_arr[idx].src="../img/icon/icon_slider_true.svg";
}

function auto_slide(){
    $(".slide_item").hide(); 
    var all_slide=$(".slide_item");
    var all_controller=$(".slider_item img");

    var now_idx=0;

    all_slide.each(function(idx, item){
        if($(this).hasClass("active")){
            now_idx=idx;
        }
    })

    let new_idx=0;
    if(now_idx===all_slide.length-1){
        new_idx=0;
    }
    else{
        new_idx=now_idx+1;
    }

    all_slide.each(function(){
        $(this).removeClass("active");
    })

    all_slide.eq(new_idx).addClass("active");
    all_slide.eq(new_idx).show();

    all_controller.each(function(){
        $(this).attr("src","../img/icon/icon_slider_false.svg");
    });

    all_controller.eq(new_idx).attr("src", "../img/icon/icon_slider_true.svg");

}