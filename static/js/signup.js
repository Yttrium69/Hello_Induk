$(document).ready(function(){
    gogo_nav();
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
    $(".user_pw").eq(1).on("propertychange change keyup paste input", function(){
        if($(".user_pw")[1].value!=$(".user_pw")[0].value){
            $(".input_pw .alert").removeClass("hide");
            $(".user_pw").eq(0).removeClass("valid");
        }
        else{
            $(".input_pw .alert").addClass("hide");
            $(".user_pw").eq(0).addClass("valid");
        }
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

async function is_valid_name(){
    const name_json={"user_name":String($(".user_name")[0].value)};
    const res=await fetch("/signup_same_name_NONO",{
        method:"POST",
        headers:{
            "Content-Type": "application/json"
        },
        body:JSON.stringify(name_json)
    });
    res_json=await res.json();
    return res_json.sameNONO;
}

async function pressded_check_name(){
    const valid_flag=await is_valid_name();
    if(valid_flag==true){
        await $(".user_name").addClass("valid");
        await $(".input_name .alert").addClass("hide");
        await $(".input_name .valid_span").removeClass("hide");
    }
    else{
        await $(".user_name").removeClass("valid");
        await $(".input_name .alert").removeClass("hide");
        await $(".input_name .valid_span").addClass("hide");
    }
}

function pressed_signup(){
    const id=$(".user_id")[0].value;
    const id_validity=$(".user_id").hasClass("valid");

    if(id_validity==false){
        alert("아이디를 중복확인하세요.");
        $(".user_id").focus();
        return;
    }

    const name=$(".user_name")[0].value;
    const name_validity=$(".user_name").hasClass("valid");
    if(name_validity==false){
        alert("닉네임을 중복확인하세요.");
        $(".user_name").focus();
        return;
    }

    const pw=$(".user_pw")[0].value;
    const pw_validity=$(".user_pw").eq(0).hasClass("valid");
    if(pw_validity==false){
        alert("비밀번호를 다시 입력하세요.");
        $(".user_pw").focus();
        return;
    }

    const form_json={"user_id":id, "user_name":name, "user_pw":pw};

    $(".form").submit();
}