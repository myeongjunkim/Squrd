function viewRecomment(obj){
    const recommentWrap = obj.parentElement.nextSibling.nextSibling.nextSibling.nextSibling;
    console.log(recommentWrap)
    console.log(obj.firstChild)
    if (recommentWrap.style.display == "none"){
        recommentWrap.style.display="block";
        obj.firstChild.style.display="none";
        obj.lastChild.style.display="inline"
    }
    else{
        recommentWrap.style.display="none";
        obj.firstChild.style.display="inline";
        obj.lastChild.style.display="none"
    }
}
   
