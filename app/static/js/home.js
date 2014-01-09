
//현재 넓이 가지고오기
function getClientWidth() {
    var ret;
    if (self.innerHeight) {     // IE 외 모든 브라우저
        ret = self.innerWidth;
    } else if (document.documentElement && document.documentElement.clientHeight) { // Explorer 6
        ret = document.documentElement.clientWidth;
    } else if (document.body) {     // IE Browser
        ret = document.body.clientWidth;
    }
    return ret;
}

//현재 넓이를 통해 리스크 트기 설정
function setWidthIntroduce(){
    var width = getClientWidth();
    var ul = document.getElementById("introduceUl");
    var li= document.getElementsByClassName('introduceLi');
    ul.style.width = width*4 + 'px';
    for ( var i=0; i<li.length; i++ ) {
        li[i].style.width = width + 'px';
    }
}

//아이디 비밀번호 에러 처리
function alertNoId() {
    document.getElementById("message").textContent = "Invalid Id";
}

function alertWrongPassword() {
    document.getElementById("message").textContent = "Wrong Password";
}



//화면 넘기기
//function scrollStart(){
//    var width = getClientWidth();
//
//    var ul = document.getElementById("introduceUl");
//    var animationInterval = 50; //10ms
//
//    move = function(){
//        var left = ul.style.left;
//        var afterLeft = parseInt(left) + width/4 + 'px' ;
//        left = afterLeft;
//    }
//    setInterval(move, animationInterval);
//}



//ajax통신
//j qurey
$(document).ready( function() {

    $("form input[type='button']").click( function() {
        return false;
    });

    $("form input[type='button']").click( function() {
        $.post("users/login", $("form").serialize(), function(data) {
            if(data=="alertNoId" || data=="alertWrongPassword") {
                window[data]();
            }
            else{
                $("form input[type='submit']").unbind("click");
                $("form input[type='submit']").click( function() { return true; });
            }
        });
    });
});

//function sendAjax(){
//    var email = document.getElementById("id_email").value;
//    var password = document.getElementById("id_password").value;
//    var obj = 'email=' + email + '&password=' + password;
//
//    request = createRequest();
//    var url = "users/login";
//    request.open ("POST", url, true);
//    request.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
//    request.onreadystatechange = checkState;
//    request.send(obj);
//
//}
////
//////소캣만들기
//function createRequest(){
//    var request = new XMLHttpRequest();
//    //다른 브라우저를 하려면은 try, catch로 에러를 통한 다른 xml통신 소켓만들기
//    return request;
//}
////
//////확인
//function checkState(){
//    if(request.readyState == 4){
//        if(request.status == 200){
//            console.log(request.responseText);
//            window[request.responseText]();
//            }
//        }
//}

function init(){
    setWidthIntroduce();
//    var loginButton = document.getElementById("loginButton");
//    loginButton.addEventListener('click', sendAjax, false);
}

window.addEventListener('load', init, false);
