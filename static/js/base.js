function gogo_url(url){
    const request = new XMLHttpRequest();
    request.open('GET', url, 'true');
    request.send();
}

function post_json_and_do(url,json, callback){
    const request=new XMLHttpRequest();
    request.onreadystatechange=function(){
        if(request.readyState==4){
            if (request.status === 200) {
                callback(request.response);
            }
        }
    }
    request.open("POST", url, true);
    console.log(json);
    request.send(JSON.stringify(json));
}
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

function toggle_hide(target){
    if(target.hasClass('show')){
        target.removeClass('show');
        target.addClass('hide');
    }
    else{
        target.addClass('show');
        target.removeClass('hide');    
    }
}

function pressed_like(self){
    toggle_icon(self);
    add_wish_list(self);
}

function toggle_icon(self){
    if(self.src[self.src.length-6]=="s"){
        self.src=self.src.slice(0, -9)+"true.svg";
    }
    else{
        self.src=self.src.slice(0, -8)+"false.svg"
    }
}

function get_category(id){
    inspector=id[0];
    if(inspector==="A") return "인형";
    else if(inspector==="B") return "돕바/과잠";
    else if(inspector==="C") return "포스터";
    else if(inspector==="D") return "텀블러/컵/문구류";
    else if(inspector==="E") return "모자/컵";
    else return "ERROR";
}

function get_category_code(name){
    if(name=="인형") return "A";
    else if(name=="돕바/과잠") return "B";
    else if(name=="포스터") return "C";
    else if(name=="텀블러/컵/문구류") return "D";
    else if(name=="모자/컵") return "E";
    else return "X";
}

function gogo_nav(){
    const header = $("#comp_banner")[0];
    const headerheight = 150;
    document.addEventListener('scroll', onScroll);
   function onScroll () {
       const scrollposition = window.scrollY;
     const nav = $('#component_navigator');
     if (headerheight<=scrollposition){
       nav.addClass('fix')
       nav.css("top", "0px")
     }
     else {
        nav.removeClass('fix')
     }
   } 
    
  }