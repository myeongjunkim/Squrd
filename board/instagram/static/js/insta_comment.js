window.onload = () =>{
    const list = document.querySelectorAll('.list');
        list.forEach((item) => 
        item.classList.remove('active'));
        list[2].classList.add('active');
}

function viewRecomment(id){
    const recommentWrap = document.querySelector('.recomment-wrap'+id);
    const obj = document.querySelector('.obj'+id)
    if (recommentWrap.style.display == "none"){
        recommentWrap.style.display="block";
        obj.firstChild.style.display="none";
        obj.lastChild.style.display="inline";
    }
    else{
        recommentWrap.style.display="none";
        obj.firstChild.style.display="inline";
        obj.lastChild.style.display="none";
    }
}




// function createRecomment(requset, perent_comment_id, user, body) {
    
//     $.ajax({
//         url: '../instagram/create-recomment/',
//         type: "Post",
//         data: {'perent_comment_id': perent_comment_id },
//         dataType : "json",
//         async: false,
//         success: function(response) {
//             // json 형태로 댓글 오면 
//         },
//         error: function() {
//             console.log("error")
//         }
//     })

// }
