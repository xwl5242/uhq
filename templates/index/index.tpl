<body>
<a href="{$topad.url}" rel="nofollow" target="_blank"><div style="width: 100%; height: 90px; background:url({$topad.img}) no-repeat center;"></div></a>
		<!--banner-->
		<div class="banner-wrap">
			<div class="container cl">
				<div class="banner-l">
					<h3>[今日推荐]</h3>
					<div class="recom">
						<div class="pbd">
							<ul>
								<volist name='today_list' id="vo">
									<li>
										<a href="{:U('/item/',array('id'=>$vo['id']))}">
											<img src="{$vo.pic_url}_400x400">
											<p>券后价：<span class="c-main">￥{$vo.coupon_price}</span></p>
											<p class="text-overflow">{$vo.title}</p>
										</a>
									</li>
								</volist>	
							</ul>
						</div>
						<div class="phd"><ul></ul></div>
					</div>
				</div>
				<div class="banner cl">
					<div class="bd">
						<ul>
							<volist name="ad_list" id="ad">   	
								<li _src="{$ad.img}" style="width: 100%;">
									<a href="{$ad.url}" target="_blank"><img src="{$ad.img}" width="760" height="338"></a>
								</li>
							</volist>
						</ul>
					</div>
					<div class="hd"><ul></ul></div>
				</div>
				<if condition="$visitor">
					<div class="banner-r">
						<div class="login">
							<a href="{:U('user/ucenter')}"><img src="{$visitor.avatar}" class="round"></a>
							<p>欢迎，<a href="{:U('user/ucenter')}" class="c-main">{$visitor.nickname}</a></p>
							<a href="{:U('user/ucenter')}" class="btn btn-pink">个人中心</a>
						</div>
						<div class="jifen flexbox">
						<div class="txt"><span class="title">直播数量</span><span>当前优惠<em>{$total_item}</em>款</span></div></div>
						</div>
					</div>
				<else/>	
					<div class="banner-r">
						<div class="login">
							<img src="__STATIC__/tqkpc/images/default.png" class="round">
							<p>提交订单换积分</p>
							<a href="{:U('login/index')}" class="btn btn-pink">立即登录</a>
						</div>
						<div class="jifen flexbox">
							<div class="txt"><span class="title">直播数量</span><span>当前优惠<em>{$total_item}</em>款</span></div></div>
						</div>
					</div>
				</if>	
			</div>
		</div>
		<script type="text/javascript">
			jQuery(".banner").slide({
			    titCell: ".hd ul",
			    mainCell: ".bd ul",
			    effect: "fold",
			    autoPlay: true,
			    autoPage: true,
			    trigger: "click",
			    startFun: function(i) {
			        var curLi = jQuery(".banner .bd li").eq(i);
			        if ( !! curLi.attr("_src")) {
			            curLi.css("background", curLi.attr("_src")).removeAttr("_src")
			        }
			    }
			});
			jQuery(".recom").slide({titCell:".phd ul",mainCell:".pbd ul",autoPlay:true,autoPage: true,});
		</script>
		<!--service-->
		<div class="service">
			<div class="container cl">
				<ul class="cl">
					<li>
						<p class="f-l">券</p>
						<div class="f-l">
							<h3 class="c-main">先领券再下单</h3>
							<h4>享现金立减优惠</h4>
						</div>
					</li>
					<li>
						<p class="f-l"><i class="iconfont icon-filter"></i></p>
						<div class="f-l">
							<h3 class="c-main">人工精选</h3>
							<h4>优质、优惠商品</h4>
						</div>
					</li>
					<li>
						<p class="f-l"><i class="iconfont icon-fuwuwuyou"></i></p>
						<div class="f-l">
							<h3 class="c-main">安全无忧</h3>
							<h4>所有交易在淘宝完成安全放心</h4>
						</div>
					</li>
					<li>
						<p class="f-l">24</p>
						<div class="f-l">
							<h3 class="c-main">每日上新</h3>
							<h4>24小时不间断上新</h4>
						</div>
					</li>
					<li>
						<p class="f-l"><i class="iconfont icon-meiyuan"></i></p>
						<div class="f-l">
							<h3 class="c-main">积分兑好礼</h3>
							<h4>提交订单就能赚积分</h4>
						</div>
					</li>
				</ul>
			</div>
		</div>
		<!--temai-->
		<div class="container cl">
			<div class="indexblock">
				<div class="hottitle">
					<p><i class="iconfont icon-fire"></i>特卖精选</p>
				</div>
				<div class="temai cl">
					<ul>
<volist name='jingxuan' id="vo">
						<li>
							<div class="item">
								<a target="_blank" href="{:U('/item/',array('id'=>$vo['id']))}" class="link">
									<img src="{$vo.pic_url}_400x400">
									<p class="text-overflow">{$vo.title}</p>
								</a>
								<div class="price">
									<p class="c-main">￥<span>{$vo.coupon_price}</span>(券后价)</p><p><del>￥{$vo.price}</del></p>
								</div>
								<div class="sales cl">
								<if condition="$vo.shop_type eq 'B'"><img src="__STATIC__/tqkpc/images/tmall.png"><else/><img src="__STATIC__/tqkpc/images/taobao.png"></if>
									<p>月销量：<span class="c-primary">{$vo.volume}</span>件</p>
								</div>
								<a target="_blank" href="{:U('/item/',array('id'=>$vo['id']))}" class="coupon">
									<h5>优惠券：<span>{$vo.quan}</span>元</h5>
									<p>立即<br>领券</p>
								</a>
							</div>
						</li>
</volist>
					</ul>
				</div>
			</div>
		</div>
		<!--hot-->
		<div class="container cl">
			<div class="indexblock">
				<div class="hottitle">
					<p><i class="iconfont icon-gift"></i>超级人气榜</p>
				</div>
				<div class="hot cl">
					<ul>
<volist name='top' id="vo">	
						<li>
							<div class="item cl">
								<div class="pic f-l mr-10">
									<a target="_blank" href="{:U('/item/',array('id'=>$vo['id']))}"><img src="{$vo.pic_url}_400x400"></a>
								</div>
								<div class="txt f-l">
									<div class="tit">
										<if condition="$vo.shop_type eq 'B'"><img src="__STATIC__/tqkpc/images/tmall.png"><else/><img src="__STATIC__/tqkpc/images/taobao.png"></if><a href="{:U('/item/',array('id'=>$vo['id']))}">{$vo.title}</a>
									</div>
									<div class="price cl">
										<p class="f-l c-main">￥<span>{$vo.coupon_price}</span><del>￥{$vo.price}</del></p>
										<p class="f-r">省<span class="c-main">{$vo.quan}</span>元</p>
									</div>
									<a target="_blank" href="{:U('/item/',array('id'=>$vo['id']))}" class="sales">月销量{$vo.volume}件</a>
								</div>
							</div>
						</li>
</volist>
					</ul>
				</div>
			</div>
		</div>
		<!--main-->
<volist name="hotsales" id="vo">
		<div class="main">
			<div class="container cl">
				<div class="color color{$vo.cid}">
					<a target="_blank" href="{:U('cate/index',array('cid'=>$vo['cid']))}" class="tit">
						<h3>{$vo.name}<i class="iconfont icon-right2"></i></h3>
						<span>{$vo.remark}</span>
					</a>
					<div class="bd">
						<ul>
							<li><a href="{:U('/item/',array('id'=>$vo['hotsale']['id']))}" target="_blank">
								<img src="{:$vo['hotsale']['pic_url']}_300x300" width="200" height="200">
								<p>{:$vo['hotsale']['title']}</p></a>
							</li>
						</ul>
					</div>
				</div>
				<div class="shop">
					<table>
						<tr>
<?php
$newsale=$vo['newsale'];	
?>
<volist name="newsale" offset="1" id="child">							
							
							<td>
								<div class="item">
									<div class="cl">
										<div class="pic f-l">
											<a target="_blank" href="{:U('/item/',array('id'=>$child['id']))}"><img src="{:$child['pic_url']}_300x300"></a>
										</div>
										<div class="txt f-l">
											<div class="price"><p>券后价</p></div>
											<p class="c-main">￥<span>{$child.coupon_price}</span></p>
											<p><if condition="$child.shop_type eq 'C' ">淘宝</if><if condition="$child.shop_type eq 'B' ">天猫</if>价：￥{$child.price}</p>
											<div class="coupon">领券省：{$child.quan}元</div>
										</div>
									</div>
									<a target="_blank" href="{:U('/item/',array('id'=>$child['id']))}" class="tit text-overflow">{$child.title}</a> 
								</div>
							</td>
<if condition="$i % 3 eq 0"></tr><tr></if>
</volist>
							
						
						</tr>
					</table>
				</div>
			</div>
		</div>
</volist>	
		
	<!--topic-->
		<div class="container cl">
			<div class="indexblock">
				<div class="hottitle">
					<p><i class="iconfont icon-fire"></i>头条资讯</p>
				</div>
				<div class="topic cl">
					<ul>
<volist name='list' id="cateid">
						<li>
							<div class="item cl">
								<div class="pic f-l">
								<a target="_blank" href="{$cateid.linkurl}" >	<img src="{$cateid.pic}"></a>
								</div>
								<div class="txt f-l">
									<a  target="_blank" href="{$cateid.linkurl}" class="tit">{$cateid.title}</a>
									<p class="details">
										{$cateid.infocontent}
									</p>
									<p>
										<span class="f-l">{$cateid.add_time}</span>
									</p>
								</div>
							</div>
						</li>
</volist>
					</ul>
				</div>
			</div>
		</div>		

<include file="public:foot" />
		<script type="text/javascript">
			var color=$(".color");
			color.each(function(){
				$(this).slide({titCell:".hd ul",mainCell:".bd ul", autoPlay: true, autoPage: true,});
			})
		</script>
<if condition="$alertadv">
<style type="text/css">
	/*activity*/
	.activity {background: transparent!important;box-shadow: none!important;}
	#activity {position: relative;display: none;}
	.activity .actbtn {background: transparent;border: none;position: absolute;top: 8%;width: 87%;height: 90%;left: 4%;}
	.activity .cancel {cursor: pointer;position: absolute;width: 30px;height: 30px;right: 50px;top: 0;}
</style>
<div id="activity">
	<img src="{$alertadv.img}" width="100%"/>
	<a href="{$alertadv.url}" rel="nofollow" target="_blank" class="actbtn"></a>
	<label class="cancel"></label>
</div>
<script type="text/javascript">
$(function(){
	layer.open({
	  type: 1,
	  title: false,
	  closeBtn: 0,
	  area: '360px',
	  offset:'25%',
	  shadeClose: true,
	  content: $('#activity'), 
	  skin: 'activity',
	  success: function(layero, index){
		$('.cancel').click(function(){
		layer.close(index);
		})
	  }
	});
});
</script>
</if> 
	</body>
</html>
