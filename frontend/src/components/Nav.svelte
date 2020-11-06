<script>
	let segment = "index";
	import ProfileDropdown from '../components/ProfileDropdown.svelte';
	import { stores } from '@sapper/app';


    const { session, page } = stores();
	console.log($page.path.split('/')[1])
	$: active = (segment.includes("index"));
</script>

{#if $page.path.split('/')[1] != 'profile' && $page.path.split('/')[1] != 'login' }
<nav>
	<ul>
		{#if active}
			<li><a href="/"  rel=prefetch>Home</a></li>
			<li><a href="popular"  rel=prefetch>Explore</a></li>
			{#if $session.user }	
				<li><a href="/feed" rel=prefetch>Feed</a></li>
				<li><a href="/profile" rel=prefetch> Profile</a></li>
			{:else}
				<li><a href="login" rel=prefetch>Login</a></li>
				<li><a href="login?signup=1" rel=prefetch>Sign Up</a></li>
			{/if}
		{/if}
			<!--<li><a href="profile" rel=prefetch>Profile</a></li>-->

		<!-- for the blog link, we're using rel=prefetch so that Sapper prefetches
		     the blog data when we hover over the link or tap it on a touchscreen -->
		<!-- <li><a rel=prefetch aria-current="{segment === 'blog' ? 'page' : undefined}" href="blog">blog</a></li>-->
	</ul>
</nav>
{/if}
<style>
	nav {
		border-bottom: 1px solid rgba(255,62,0,0.1);
		font-weight: 300;
		padding: 0 1em;
		color: white;
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

	a {
		text-decoration: none;
		padding: 1em 0.5em;
		display: block;
	}
</style>