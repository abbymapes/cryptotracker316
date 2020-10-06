<script>


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

hi