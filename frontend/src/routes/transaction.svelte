
<script>
  import { goto,stores } from '@sapper/app';
  import { onMount } from "svelte";
  import Leftbar from "../components/Leftbar.svelte";


  const currencies = ["BTC","ETH","LTC"]
  const { page, session } = stores();
  const { slug } = $page.params;

  export let currentUsername
  export let falcon = false
  export let loggedIn = true
  let currentUser
  let currentUid

  $: if ($session.ux) {
    currentUsername = $session.ux
    loggedIn = true
  }

  $: if (!$session.user) {
      goto('login')
  }

  $: if (!currentUser) {
    goto('login')
  }

  onMount(()=>{currentUid = firebase.auth().currentUser ? firebase.auth().currentUser.uid : undefined})

async function trans() {
    // Add a new document in collection "cities"
    currentUid.
    firebase.firestore().collection("transaction").doc().set({
        amount: 1,
        caption: "hello",
        comment_count: 0,
        like_count: 0,
        stock: "BTC",
        time: firebase.firestore.FieldValue.serverTimestamp(),
        type: "buy",
        uid: currentUid

    })
    .then(function() {
        console.log("Document successfully written!");
    })
    .catch(function(error) {
        console.error("Error writing document: ", error);
});

}
</script>

<head>
  <title>New Transaction</title>
</head>

<main>
  <div class="menu">
    <Leftbar {falcon} {loggedIn}/>
  </div>
  <div class = "content">
    <div class = "header">New Transaction</div>

    <!--Content goes here-->
    <button on:click={trans}>
      Add Comment
    </button>

  </div>
</main>

<style>
  /* Container to center page on a screen */

  .content {
  padding: 40px;
  }

  .header {
  font-size: 30px;
  color:#65ACFF;
  text-align: center;
  font-family: inherit;
  }

  a {
  display: block;
  color: hsl(210, 35%, 70%);
  text-align: center;
  padding: 15px 15px;
  text-decoration: none;
  font-size: 18px;
  }

  a:hover {
  color: #65ACFF;
  }
  main{
  display: grid;
  grid-auto-flow: column;
  grid-template-columns: 80px minmax(300px,1500px) 1fr;
  background-color: #121212;
  color: white;
  width: 100%;
  }
</style>




