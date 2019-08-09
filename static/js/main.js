$(function(){
    $('.navigation ul>li').click(function(){
        $(this).siblings().removeClass('cur')
        $(this).addClass('cur')
    });
    $('.series ul>li').click(function(){
        $(this).siblings().removeClass('cur')
        $(this).addClass('cur')
    });
});