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
  <title>Feed</title>
</head>

<TransactionPost/>
<br>
<TransactionPost/>
<br>
<TransactionPost/>
<br>
