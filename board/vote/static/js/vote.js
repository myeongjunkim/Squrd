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
                voteTotal(id)
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

function voteTotal(id){
    // 장고한테 쿼리 몇개 나오는지 달라고 요청
    $.ajax({
        url: '../vote/vote-total/',
        type: "GET",
        data: {"votePostId":id},
        dataType : "json",
        async: false,
        success: function(response) {
            console.log(response)
            changeTotal(response, id)
        },
        error: function() {
            console.log("Total func error")
        }
    })
}

function changeTotal(response, id){
    const voteFormName = '.voteForm'+id;
    const voteFormTag = document.querySelector(voteFormName);
    const voteTotalDiv = voteFormTag.querySelector('.vote-total');
    
    const leftTotalDiv = voteTotalDiv.querySelector('.left');
    const rightTotalDiv = voteTotalDiv.querySelector('.right');
    const CenterTotalDiv = voteTotalDiv.querySelector('.vote-center');

    leftTotalDiv.style.width = String(response['first']['per']) +'%';
    rightTotalDiv.style.width = String(response['second']['per']) +'%';

    leftTotalDiv.querySelector('span').innerText = response['first']['cnt'] + '명 (' + response['first']['per'] +'%)';
    rightTotalDiv.querySelector('span').innerText = response['second']['cnt'] + '명 (' + response['second']['per'] +'%)';
    CenterTotalDiv.querySelector('span').innerText = response['total'] + '명';


}




window.onload = () => {
    const inputs = document.querySelectorAll(".votePostId")
    console.log(inputs)
    for (var i=0; i<inputs.length; i++) {
        voteTotal(inputs[i].value);       

    }
}