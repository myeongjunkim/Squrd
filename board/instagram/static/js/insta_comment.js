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


window.onload = () =>{
    const list = document.querySelectorAll('.list');
        list.forEach((item) => 
        item.classList.remove('active'));
        list[2].classList.add('active');
}