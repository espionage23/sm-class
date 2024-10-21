//제이쿼리 선언
let num=0;
let num2=0;
$(function(){

  //우측버튼
$("#right").click(function(){
  // alert("right");
  if(num>=900){
    alert("오른쪽 끝에 도달함")
    return false;
  }
  $("#box").stop();
  num += 100;
  num2 += 360;
  $("#box").animate({
    left: num, "rotate": num2+"deg" 
  },1000);
});//우측버튼


//좌측버튼
$("#left").click(function(){
  // alert("left");
  if(num<=0){
    alert("왼쪽 끝에 도달함")
    return false;
  }
  $("#box").stop();
  num -= 100;
  num2 -= 360;
  $("#box").animate({
    left: num, "rotate": num2+"deg" 
  },1000);
});//좌측버튼

});//제이쿼리 선언