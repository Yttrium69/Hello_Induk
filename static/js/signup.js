function check_id(){
    // function change_checked_result(data){
    //     result=JSON.parse(data);
    //     if(result[0].sameNONO==true){
    //         $(".user_id").attr("check_result", "true");
    //         console.log("TRue");
    //     }
    //     else{
    //         $(".user_id").attr("check_result","false");
    //         console.log("false");
    //     }
    // }
    // const id_json=[{"user_id":$(".user_id")[0].value}];
    // console.log(id_json)
    // post_json_and_do("/signup_same_id_NONO", id_json, change_checked_result);

    const id_json=[{"user_id":$(".user_id")[0].value}];
    fetch("/signup_same_id_NONO",{
        method:"POST",
        headers:{
            "Content-Type": "application/json"
        },
        body:JSON.stringify(id_json)
    })
    .then(function(res){
        console.log(res);
    })
}
