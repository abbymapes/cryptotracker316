<script>
	import Hoverable from './Hoverable.svelte';
</script>


<dropdown>
	<Hoverable let:hovering={active}>
		<div class:active>
			{#if active}
				<a href="profile" rel=prefetch>Profile</a>
				<a href="portfolio">Portfolio</a>
				<a href="balance">Add Balance</a>
				<a href = "logout">Logout</a>
			{:else}
				<a href="profile">Profile</a>
			{/if}
		</div>
	</Hoverable>
</dropdown>

<style>
	a {
		text-decoration: none;
		padding: 1em 0.5em;
		display: block;
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
</style>