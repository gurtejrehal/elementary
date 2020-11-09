$(()=>{
  
  let rotation = 0;
  let faded = 2;
  let hasKey = false;
  
  $('.turnright').on('mouseover',function(){
    rotation += 90;
    $('.assembly').css('transform','rotateY('+rotation+'deg)');
    $('.plane'+faded).delay(800).fadeIn();
    faded += 1;
    faded = faded % 4;
    $('.plane'+faded).fadeOut();   
  });
  
  $('.turnleft').on('mouseover',function(){
    rotation -= 90;
    $('.assembly').css('transform','rotateY('+rotation+'deg)');
    $('.plane'+faded).delay(800).fadeIn();
    faded -= 1;
    if(faded == -1){faded = 3; console.log('if');}
    $('.plane'+faded).fadeOut();
  });

$('.turnright').on('vmouseover',function(){
    rotation += 90;
    $('.assembly').css('transform','rotateY('+rotation+'deg)');
    $('.plane'+faded).delay(800).fadeIn();
    faded += 1;
    faded = faded % 4;
    $('.plane'+faded).fadeOut();   
  });
  
  $('.turnleft').on('vmouseover',function(){
    rotation -= 90;
    $('.assembly').css('transform','rotateY('+rotation+'deg)');
    $('.plane'+faded).delay(800).fadeIn();
    faded -= 1;
    if(faded == -1){faded = 3; console.log('if');}
    $('.plane'+faded).fadeOut();
  });
  
  $('.doorknob').on('click',function(){
    if(hasKey === true){
      alert('.--- . -.-. .-.. .- - .. ... --- -.');
    }else{
    console.log('Locked.');
  }
  });
  $('.key').on('click',function(){
    $(this).fadeOut();
    hasKey = true;
  });

});
