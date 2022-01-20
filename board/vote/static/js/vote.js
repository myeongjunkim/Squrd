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

function changeBorder(){
    const input_1 = document.getElementById("contactChoice1")
    const input_2 = document.getElementById("contactChoice2")
    if (input_1.checked){
        document.getElementById("label1").style.border="2px solid #041562"
        document.getElementById("label2").style.border="0px solid #041562"
    }
    else if(input_2.checked){
        document.getElementById("label2").style.border="2px solid #041562"
        document.getElementById("label1").style.border="0px solid #041562"
   
    }
}

    