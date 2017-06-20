

$(document).ready(function(){
	$(window).on("scroll",function(){
  	var wn = $(window).scrollTop();
    if(wn > 120){
    	$(".navbar").css({"background":"#131313"});
      $(".navbar-brand").css({"color":"white"});
      $("#imgWrapper").css({"box-shadow": "10px 10px 5px #f8f8f8"});
    }
    else{
    	$(".navbar").css({"background":"#f8f8f8"});
      $(".navbar-brand").css({"color":"black"});
    }
  });
});