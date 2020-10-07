<script>
	export let segment;
</script>


<nav>
	<ul>
		<li><a href="/"  rel=prefetch>home</a></li>
		<li><a href="login" rel=prefetch>login</a></li>
		<li><a href="login?signup=1" rel=prefetch>signup</a></li>

		<!-- for the blog link, we're using rel=prefetch so that Sapper prefetches
		     the blog data when we hover over the link or tap it on a touchscreen -->
		<li><a href="profile"  rel=prefetch>profile</a></li>
	</ul>
</nav>


<style>
	nav {
		border-bottom: 2px solid #222222;
			padding:10px;

	}
	ul{
		display: inline;
		list-style: none;
	}
	li{
		float: left;
		margin-right: 30px;
	}


</style>