$(document).ready(function(){
    $(".input_id input").on("propertychange change keyup paste input", function(){
        $(".input_id .alert").addClass("hide");
        $(".user_id").removeClass("valid");
        $(".input_id .valid_span").addClass("hide");
    });
    $(".input_name input").on("propertychange change keyup paste input", function(){
        $(".input_name .alert").addClass("hide");
        $(".user_name").removeClass("valid");
        $(".input_name .valid_span").addClass("hide");
    });
})
async function is_valid_id(){
    const id_json={"user_id":String($(".user_id")[0].value)};
    const res=await fetch("/signup_same_id_NONO",{
        method:"POST",
        headers:{
            "Content-Type": "application/json"
        },
        body:JSON.stringify(id_json)
    });
    res_json=await res.json();
    return res_json.sameNONO;
}

async function pressded_check_id(){
    const valid_flag=await is_valid_id();
    console.log(valid_flag)
    if(valid_flag==true){
        await $(".user_id").addClass("valid");
        await $(".input_id .alert").addClass("hide");
        await $(".input_id .valid_span").removeClass("hide");
    }
    else{
        await $(".user_id").removeClass("valid");
        await $(".input_id .alert").removeClass("hide");
        await $(".input_id .valid_span").addClass("hide");
    }
}
