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

function changeBorder(id){
    const voteFormName = '.voteForm'+id;
    const voteFormTag = document.querySelector(voteFormName);
    
    const input_1 = voteFormTag.querySelector('#contactChoice'+id+'-1')
    const input_2 = voteFormTag.querySelector('#contactChoice'+id+'-2')
    
    if (input_1.checked){
        voteFormTag.querySelector('.vote-left .vote-card').style.border="3px solid yellow";
        voteFormTag.querySelector('.vote-right .vote-card').style.border="0px solid yellow";
    }
    else if(input_2.checked){
        voteFormTag.querySelector('.vote-right .vote-card').style.border="3px solid yellow";
        voteFormTag.querySelector('.vote-left .vote-card').style.border="0px solid yellow";
    };
}


function voteForm(id) {
    const result = getRadioValue(id)
    if (!result){
        return alert("사진을 눌러 선택해주세요!");
    }
    console.log(result);
    $.ajax({
        url: '../vote/create-participant/',
        type: "GET",
        data: {'result': result, "votePostId":id},
        dataType : "text",
        async: false,
        success: function(response) {
            if(response == 'create') {
                alert("투표 완료!");
                // 투표 선택 못하도록
                // 중복 투표 안되도록
                // 투표율 집계
            } else if(response == 'overlap') {
                alert("중복 참여는 안돼요 :(")
            }
        },
        error: function() {
            console.log("error")
        }
    })

    
    
}

function getRadioValue(id) {
    const inputClass = '.contactChoice'+id;
    var obj_length = document.querySelectorAll(inputClass).length;
    for (var i=0; i<obj_length; i++) {
        if (document.querySelectorAll(inputClass)[i].checked == true) {
                return document.querySelectorAll(inputClass)[i].value;
            }
        }
}