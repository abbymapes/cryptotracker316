
<script>
	let user = undefined
	import firebase from 'firebase/app'
	import {onMount} from 'svelte'
	onMount(()=>{
		firebase.auth().onAuthStateChanged(u=>{
			if(u)
			user = u
		})
	})

</script>


{#if user}
	<h1>Hello {user.email}</h1>
{/if}
<h1> <a href="login"  rel=prefetch>login</a> </h1>