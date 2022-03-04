// 'use strict';

// var Trail = function(options) {
//   this.size        = options.size || 50;
//   this.trailLength = options.trailLength || 20;
//   this.interval    = options.interval || 15;
//   this.hueSpeed    = options.hueSpeed || 6;

//   this.boxes = [];
//   this.hue   = 0;
//   this.mouse = {
//     x : window.innerWidth/2,
//     y : window.innerHeight/2
//   };

//   this.init = function() {
//     let body = document.querySelector('body');
//     for (var i = 0; i < this.trailLength; i++) {
//       this.boxes[i]              = document.createElement('div');
//       this.boxes[i].className    = 'box';
//       this.boxes[i].style.width  = this.size + 'px';
//       this.boxes[i].style.height = this.size + 'px';
//       body.appendChild(this.boxes[i])
//     }

//     var self = this;

//     // document.onmousemove = function() {
//     //   event = event || window.event;
//     //   self.mouse.x = event.clientX;
//     //   self.mouse.y = event.clientY;
//     //   console.log(event);
//     // };

//     //Periodically update mouse tracing and boxes
//     setInterval(function(){
//       self.updateHue();
//       self.updateBoxes();
//     }, this.interval);
//   }

//   //Update hue and constrain to 360
//   this.updateHue = function() {
//     this.hue = (this.hue + this.hueSpeed) % 360;
//   }

//   //Update box positions and stylings
//   this.updateBoxes = function() {
//     for (var i = 0; i < this.boxes.length; i++) {
//       if (i+1 === this.boxes.length) {
//         this.boxes[i].style.top             = this.mouse.y - this.size/2 + 'px';
//         this.boxes[i].style.left            = this.mouse.x - this.size/2 + 'px';
//         this.boxes[i].style.backgroundColor = 'hsl(' + this.hue + ', 90%, 50%)';
//       } else {
//         this.boxes[i].style.top             = this.boxes[i+1].style.top;
//         this.boxes[i].style.left            = this.boxes[i+1].style.left;
//         this.boxes[i].style.backgroundColor = this.boxes[i+1].style.backgroundColor;
//       }
//     }
//   }
// }

// window.onload = () =>{
//     let body = document.querySelector('body');
//     let responsiveDiv = document.querySelector('.rendering-container');

//     var options = {
//         trailLength: 20,
//         size: 20,
//         interval: 10,
//         hueSpeed: 2,
//     };
//     var trail = new Trail(options);
//     trail.init();

//     // function addEffect(e) {
//     //     console.log("dd")
//     //     trail.mouse.x = e.clientX;
//     //     trail.mouse.y = e.clientY;
//     // };
    

        
//     body.addEventListener('mousemove', (event) => {
//         trail.mouse.x = event.clientX;
//         trail.mouse.y = event.clientY;
//     });


//     responsiveDiv.addEventListener('scroll', (event) => {
//         console.log(event)
//         trail.mouse.x = event.clientX;
//         trail.mouse.y = event.clientY;
//     });
// }



//Hotfix



$(document).ready(function(){
  
    var mousePos = {};
  
   function getRandomInt(min, max) {
     return Math.round(Math.random() * (max - min + 1)) + min;
   }
    
    $(window).mousemove(function(e) {
      mousePos.x = e.pageX;
      mousePos.y = e.pageY;
    });
    
    $(window).click(function(e) {
      mousePos.x = -1;
      mousePos.y = -1;
    });
    
    var draw = setInterval(function(){
      if(mousePos.x > 0 && mousePos.y > 0){
        
        var range = 10;
        
        var color = "background: rgb("+getRandomInt(0,255)+","+getRandomInt(0,255)+","+getRandomInt(0,255)+");";
        
        var sizeInt = getRandomInt(10, 15);
        size = "height: " + sizeInt + "px; width: " + sizeInt + "px;";
        
        var left = "left: " + getRandomInt(mousePos.x-range-sizeInt, mousePos.x+range) + "px;";
        
        var top = "top: " + getRandomInt(mousePos.y-range-sizeInt, mousePos.y+range) + "px;"; 
  
        var style = left+top+color+size;
        $("<div class='ball' style='" + style + "'></div>").appendTo('#body').one("webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend", function(){$(this).remove();}); 
      }
    }, 50);
  });
  



function clickEffect(e){
    var d=document.createElement("div");
    d.className="clickEffect";
    d.style.top=e.clientY+"px";d.style.left=e.clientX+"px";
    document.body.appendChild(d);
    d.addEventListener('animationend',function(){d.parentElement.removeChild(d);}.bind(this));
}
document.addEventListener('click',clickEffect);
