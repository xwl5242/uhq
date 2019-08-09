$(function(){
    $('.navigation ul>li').click(function(){
        $(this).siblings().removeClass('cur');
        $(this).addClass('cur');
    });
    $('.series ul>li').click(function(){
        $(this).siblings().removeClass('cur');
        $(this).addClass('cur');
    });
    $('.search input:eq(1)').click(function(){
        let kw = $('input[name="k"]').val();
        if(kw){
            window.location.href = '/q-k/'+kw;
        }
    });
});