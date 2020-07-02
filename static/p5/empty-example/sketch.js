// var blue = n
document.cookie = "rectcolor=#108DE0";

function setup() {
  createCanvas(900, 900);
  background(220)
}


function draw() {
  


  if (mouseIsPressed) {
    drawrect()
  } else {
    
  }
  
}

// draw rect
function drawrect(){
  var rectcolor = getCookie("rectcolor")
  // print(cook)
  fill(color(rectcolor))
  rect(mouseX-50, mouseY-50, 80, 80);
  textSize(32);
  // text(cook,50,100);
}


bluerect = new Object()
bluerect




// get info from Cookie
function getCookie(cname){
   var arr = document.cookie.match(new RegExp("(^| )"+cname+"=([^;]*)(;|$)"));
  if(arr != null) return unescape(arr[2]); return null;
}