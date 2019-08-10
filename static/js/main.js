$(function(){
    $('.navigation ul>li').click(function(){
        $(this).siblings().removeClass('cur');
        $(this).addClass('cur');
    });
    $('.series ul>li').click(function(){
        $(this).siblings().removeClass('cur');
        $(this).addClass('cur');
    });
    $('.search input:eq(1),#m_search_btn').click(function(){
        let kw = $('input[name="k"]').val();
        if(kw){
            window.location.href = '/q-k/'+kw;
        }
    });
});