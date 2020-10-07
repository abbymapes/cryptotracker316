<script>
	export let segment;
</script>

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

	/* Dropdown menu */
	.dropdown {
	  float: right;
	  overflow: hidden;
	}

	.dropdown-content {
	  display: none;
	  position: absolute;
	  background-color: #f9f9f9;
	  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
	  z-index: 1;
	}

	.dropdown-content a {
	  float: none;
	  text-decoration: none;
	  display: block;
	  text-align: left;
	}

	.dropdown-content a:hover {
	  background-color: #ddd;
	}

	.dropdown:hover .dropdown-content {
	  display: block;
	}
</style>

<nav>
	<ul>
		<li><a aria-current="{segment === 'feed' ? 'page' : undefined}" href="/authUser/feed">Feed</a></li>
		<li><a aria-current="{segment === 'search' ? 'page' : undefined}" href="/authUser/search">Search</a></li>
		<li><a aria-current="{segment === 'popular' ? 'page' : undefined}" href="/authUser/popular">Popular</a></li>

		<li>
    	<div class = "dropdown">
	    	<a aria-current="{segment === 'profile' ? 'page' : undefined}" href="/authUser/profile">Profile</a>
			<div class="dropdown-content">
	      		<li><a aria-current="{segment === 'portfolio' ? 'page' : undefined}" href="/authUser/portfolio">Portfolio</a></li>
	      		<br>
	      		<li><a aria-current="{segment === 'balance' ? 'page' : undefined}" href="/authUser/balance">Add Balance</a></li>
	      		<br>
	      		<li><a href="/">Logout</a></li>
	    	</div>
	    </div>
	    </li>

		<!-- for the blog link, we're using rel=prefetch so that Sapper prefetches
		     the blog data when we hover over the link or tap it on a touchscreen -->
		<!-- <li><a rel=prefetch aria-current="{segment === 'blog' ? 'page' : undefined}" href="blog">blog</a></li>-->
	</ul>
</nav>
