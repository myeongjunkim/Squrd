  const random_char = () => {
    const arr = [...Array(100).keys()].map(key => key + 1)
    return arr[Math.floor(Math.random() * 100)];
  };
  
  const random_op = () => {
    const masked = [];

    const possible = "+-x"
    const op = possible.charAt(Math.floor(Math.random() * possible.length));
    masked.push(op);
    
    return masked.join('');

   
  };


  const mask = (chars) => {
    const masked = [];
  
    // for (let i = 0; i < chars.length; i++) {
    //     masked.push(random_char());
    // }
    masked.push(random_char());
    
    return masked.join('');
  };

  
  
  const shuffle = el => {
    const chars = el.textContent.split('');
    anime({
      delay: 1000,
      duration: 1000,
      easing: 'easeInQuad',
      update: () => {
        el.textContent = mask(chars);
      },
      complete: () => {
        el.classList.add('completed');
        el.removeAttribute('onclick');
        if (document.querySelectorAll('.completed').length == 3){
            document.querySelector('.lever-wrap').setAttribute('onclick','leverClick()')
            document.querySelector('.lever-wrap .lever').classList.add('animated')


        }
      }
    });
    
  };


  function leverClick(){
    document.querySelector('.lever-wrap .lever').classList.remove('animated')
    
    setTimeout(function() {
        document.querySelector('.lever-wrap').classList.add('clicked');
        setTimeout(getResult, 800);
    }, 500)
       
    
    
    
    setTimeout(viewResult, 4000);
  }

  function getResult(){
      let ops = document.querySelectorAll('.op')
      anime({
        delay: 2000,
        duration: 2000,
        easing: 'easeInQuad',
        update: () => {
          ops[0].textContent = random_op();
          ops[1].textContent = random_op()
        },
        complete: () => {
          ops[0].classList.add('opEnd');
          ops[1].classList.add('opEnd');
        }
      });

  }

 

  function viewResult(){
      const resultComponents = document.querySelectorAll('.resultText');
      let result = "";
      for(var span of resultComponents){
          console.log(span)
          let text = span.innerText
          if ( text == 'x'){
            result = result + '*';
          } else{
            result = result+text;
          }
            

      }
      console.log(result)
      const resultSpan = document.querySelector('.machine-result span')
      resultSpan.style.fontSize = '30px';
      resultSpan.innerText = eval(result) + " 점 획득!";
      resultSpan.classList.add('resultEnd');
  }
  
