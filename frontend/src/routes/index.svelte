


<script>

	import { stores } from '@sapper/app';
	import { onMount } from "svelte";

	const {session} = stores()
	onMount( async()=>{
		 fetch('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
		.then(res=>res.json())
		.then(data => console.log(data));
		
	})

</script>
{#if $session.user}
	<h1>Logged In</h1>
{/if}
