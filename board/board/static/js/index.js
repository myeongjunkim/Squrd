function clickBtn(){
    const cards = document.querySelectorAll('.card');
    const i = Math.floor(Math.random() * 3);
    cards[i].classList.toggle('disable')
    
}