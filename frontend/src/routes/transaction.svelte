<script>
  import { onMount } from "svelte";
  import Leftbar from "../components/Leftbar.svelte";

  import { goto, stores } from '@sapper/app';
  const {page,session} = stores();
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

  onMount(async()=>{
    firebase.auth().onAuthStateChanged(function(user) {
  		if (user) {
			  u = user.uid;
			  var docRef = firebase.firestore().collection("users").doc(user.uid);
			  docRef.get().then(function(doc) {
          if (doc.exists) {
            currentUsername = docRef.data().username
          } else {
            goto('login')
            console.log("No such document!");
          }
        }).catch(function(error) {
          console.log("Error getting document:", error);
          goto('login')
        });
  		} else {
        goto('login')
  	  }
  })})
</script>

<head>
  <title>New Transaction</title>
</head>
<!--Content goes here-->

<main>
  <div class="menu">
    <Leftbar {falcon} {loggedIn}/>
  </div>
  <div class = "content">
    <div class = "header">New Transaction</div>
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