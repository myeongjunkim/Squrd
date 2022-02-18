
window.onload = () =>{

    const body = document.querySelector('body');
    const modal = document.querySelector('.modal-newPost');
    const btnOpenPopup = document.querySelector('.btn-open-popup');
    
    btnOpenPopup.addEventListener('click', () => {
        modal.classList.toggle('show');
        if (modal.classList.contains('show')) {
            body.style.overflow = 'hidden';
        }
    });

    modal.addEventListener('click', (event) => {
        if (event.target === modal) {
            modal.classList.toggle('show');

            if (!modal.classList.contains('show')) {
                body.style.overflow = 'auto';
            }
        }
    });





    const list = document.querySelectorAll('.list');
      list.forEach((item) => 
      item.classList.remove('active'));
      list[2].classList.add('active');
}


function changeImg(event,Img) {
    var reader = new FileReader();

    reader.onload = function (event) {
        // get loaded data and render thumbnail.
        document.getElementById(Img).src = event.target.result;
    };
    console.log(event)
    // read the image file as a data URL.
    reader.readAsDataURL(event.target.files[0]);
};