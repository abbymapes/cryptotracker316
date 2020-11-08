
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

  onMount(()=>{
	firebase.auth().onAuthStateChanged(function(user) {
  		if (user) {
			loggedIn = true
			u = user.uid;
			var docRef = firebase.firestore().collection("users").doc(user.uid);

			docRef.get().then(function(doc) {
    		if (doc.exists) {
			console.log("Document data:", doc.data());
			balance = doc.data().balance;
			console.log(balance)

    		} else {
				// doc.data() will be undefined in this case
				goto('login')
				console.log("No such document!");
    		}
			}).catch(function(error) {
				goto('login')
    			console.log("Error getting document:", error);
			});

    // User is signed in.
  		} else {
			goto('login')
    	// No user is signed in.
  		}
	});
})


    
    function buy() {
	var sfDocRef = firebase.firestore().collection("users").doc(u);
	return firebase.firestore().runTransaction(function(transaction) {
    return transaction.get(sfDocRef).then(function(sfDoc) {
        if (!sfDoc.exists) {
            throw "Document does not exist!";
        }

		if (balance >= (n*cryptoPrice)) { //needs to be user balance
            //Update document to show ownership of x amount of crypto
        } else {
            return Promise.reject("Transaction failed: Not Enough balance!");
        }
    });

	}).then(function() {
    	alert("Transaction successfully committed!");
	}).catch(function(error) {
    	alert("Transaction failed: Not Enough balance!", error);
	});
    alert('Balance Added!');
	}

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




