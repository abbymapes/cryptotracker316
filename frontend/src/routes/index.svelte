


<script>

	import { stores } from '@sapper/app';

	const {session} = stores()


</script>
{#if $session.user}
	<h1>Logged In</h1>
{/if}
