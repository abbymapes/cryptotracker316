<script>
	export let segment;
	import ProfileDropdown from '../components/ProfileDropdown.svelte';
	import { stores } from '@sapper/app';


    const { session } = stores();

	$: active = (segment.includes("authUser") );
</script>


<nav>
	<ul>
		{#if active}
			<li><a aria-current="{segment === '/authUser/feed' ? 'page' : undefined}" href="/authUser/feed">Feed</a></li>
			<li><a aria-current="{segment === '/authUser/search' ? 'page' : undefined}" href="/authUser/search">Search</a></li>
			<li><a aria-current="{segment === '/authUser/popular' ? 'page' : undefined}" href="/authUser/popular">Popular</a></li>
			<li><a aria-current="{segment === '/authUser/transaction' ? 'page' : undefined}" href="/authUser/transaction">New Transaction</a></li>
			<li><ProfileDropdown/></li>
		{:else}
			<li><a href="/"  rel=prefetch>Home</a></li>
			{#if $session.user }	
			<li><a href="profile" rel=prefetch>Profile</a></li>
			<li><a href="/authUser/feed" rel=prefetch>Feed</a></li>
			{:else}
			<li><a href="login" rel=prefetch>Login</a></li>
			<li><a href="login?signup=1" rel=prefetch>Sign Up</a></li>
			{/if}
			<!--<li><a href="profile" rel=prefetch>Profile</a></li>-->
		{/if}

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