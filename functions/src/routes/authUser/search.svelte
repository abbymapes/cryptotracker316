<script>
  import TransactionPost from '../../components/TransactionPost.svelte';
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

<style>
</style>

<head>
  <title>Search</title>
</head>

<div class="header">Search</div>
<!--Content goes here-->