const clickUpdateBtn = () =>{
    $.ajax({
        type: "POST",
        url: "../../makearticle.py",
        data: {}
      }).done(function( o ) {
        location.href = '/update_article';
      });
}