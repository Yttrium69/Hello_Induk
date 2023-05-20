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