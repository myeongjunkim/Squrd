function changeImg(event, backgroundImg) {
    var reader = new FileReader();

    reader.onload = function (event) {
        // get loaded data and render thumbnail.
        document.getElementById(backgroundImg).style.backgroundImage = "url("+event.target.result+")";
    };
    console.log(event)
    // read the image file as a data URL.
    reader.readAsDataURL(event.target.files[0]);
};

function changeBorder(obj){
    const contentsDiv = obj.parentElement;
    const input_1 = contentsDiv.children[0].children[1];
    const input_2 = contentsDiv.children[2].children[1];

    if (input_1.checked){
        contentsDiv.children[0].children[0].style.border="3px solid yellow";
        contentsDiv.children[2].children[0].style.border="0px solid yellow";
    }
    else if(input_2.checked){
        contentsDiv.children[2].children[0].style.border="3px solid yellow";
        contentsDiv.children[0].children[0].style.border="0px solid yellow";
   
    };
}

function setAttr(){
    const labelTag = document.querySelectorAll('.addAttrLabel');
    const inputTag = document.querySelectorAll('.addAttrInput');
    for(var i=0;i<labelTag.length;i++){
        labelTag[i].setAttribute( 'for', 'contactChoice'+i )
        inputTag[i].setAttribute( 'id', 'contactChoice'+i )
    }
}

window.onload = () =>{
    setAttr();
}

function voteForm() {
    // 일반화 필요, 선택 여부 필요
    const result = document.querySelector('.result').value;
    const votePostId = document.querySelector('.vote-post-id').value;
    $.ajax({
        url: '../vote/create-participant/',
        type: "GET",
        data: {'result': result, "votePostId":votePostId},
        dataType : "text",
        async: false,
        success: function(response) {
            if(response == 'create') {
                alert("성공");
            }
        },
        error: function() {
            console.log("error")
        }
    })
    
}



function getRadioValue(event) {
    // 일반화 필요
    document.querySelector('.result').value = 
      event.target.value;
  }

