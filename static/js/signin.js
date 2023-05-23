function pressed_signin(){
    const id_area=$(".user_id");
    const pw_area=$(".user_pw");

    if(id_area.val()==""){
        alert("아이디를 입력하세요.");
        return;
    }
    else if(pw_area.val()==""){
        alert("패스워드를 입력하세요.");
        return;
    }
    
    $(".form").submit();
}