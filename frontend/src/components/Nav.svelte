<script>
	export let segment;
	import ProfileDropdown from '../components/ProfileDropdown.svelte';
</script>


<nav>
	<ul>
		<li><a aria-current="{segment === 'feed' ? 'page' : undefined}" href="/authUser/feed">Feed</a></li>
		<li><a aria-current="{segment === 'search' ? 'page' : undefined}" href="/authUser/search">Search</a></li>
		<li><a aria-current="{segment === 'popular' ? 'page' : undefined}" href="/authUser/popular">Popular</a></li>
		<li><a aria-current="{segment === 'transaction' ? 'page' : undefined}" href="/authUser/transaction">New Transaction</a></li>
		<!-- <li><ProfileDropdown/></li> -->
		<li><a href="/"  rel=prefetch>home</a></li>
		<li><a href="login" rel=prefetch>login</a></li>
		<li><a href="login?signup=1" rel=prefetch>signup</a></li>
		<li><a href="profile" rel=prefetch>Profile</a></li>

		<!-- for the blog link, we're using rel=prefetch so that Sapper prefetches
		     the blog data when we hover over the link or tap it on a touchscreen -->
		<!-- <li><a rel=prefetch aria-current="{segment === 'blog' ? 'page' : undefined}" href="blog">blog</a></li>-->
	</ul>
</nav>

<style>
	nav {
		border-bottom: 1px solid rgba(255,62,0,0.1);
		font-weight: 300;
		padding: 0 1em;
	}

	ul {
		margin: 0;
		padding: 0;
	}

	/* clearfix */
	ul::after {
		content: '';
		display: block;
		clear: both;
	}

	li {
		display: block;
		float: left;
	}

	[aria-current] {
		position: relative;
		display: inline-block;
	}

	[aria-current]::after {
		position: absolute;
		content: '';
		width: calc(100% - 1em);
		height: 2px;
		background-color: rgb(255,62,0);
		display: block;
		bottom: -1px;
	}

	a {
		text-decoration: none;
		padding: 1em 0.5em;
		display: block;
	}
</style>