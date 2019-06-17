var $els = $('.menu a, .menu p, .menu header');
var count = $els.length;
var grouplength = Math.ceil(count/3);
var groupNumber = 0;
var i = 1;
$('.menu').css('--count',count+'');
$els.each(function(j){
 if ( i > grouplength ) {
     groupNumber++;
     i=1;
 }
 $(this).attr('data-group',groupNumber);
 i++;
});

$('.menu footer button').on('click',function(e){
 e.preventDefault();
 $els.each(function(j){
     $(this).css('--top',($(this)[0].getBoundingClientRect().top - 90) + ($(this).attr('data-group') * - 15) - 20);
     $(this).css('--delay-in',j*.05+'s');
     $(this).css('--delay-out',(count-j)*.05+'s');
 });
 $('.menu').toggleClass('closed');
 e.stopPropagation();
});
