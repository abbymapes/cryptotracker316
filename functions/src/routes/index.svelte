<script>

	import firebase from 'firebase/app'

	import { onMount } from "svelte";
	onMount(()=>{
		const db =  firebase.firestore()
		db.collection("test").get().then(snap =>{
			snap.forEach(item=>{
				 console.log(item.id, " => ", item.data());
			})
		})
	})

</script>
<svelte:head>
	<title>Sapper project template</title>
</svelte:head>

<h1>Crypto Tracker</h1>



<p>
	<b> Basic Starter Template.</b>
</p>
