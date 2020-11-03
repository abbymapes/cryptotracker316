<script>
let selected = 	{ id: 1, text: `Add Balance` };
$: console.log(selected)
import { onMount } from 'svelte';	
let u;

onMount(()=>{
	firebase.auth().onAuthStateChanged(function(user) {
  		if (user) {
			  u = user.uid;
			var docRef = firebase.firestore().collection("users").doc(user.uid);

			docRef.get().then(function(doc) {
    		if (doc.exists) {
			console.log("Document data:", doc.data());
			balance = doc.data().balance;
			console.log(balance)

    		} else {
        	// doc.data() will be undefined in this case
        	console.log("No such document!");
    		}
			}).catch(function(error) {
    		console.log("Error getting document:", error);
			});

    // User is signed in.
  		} else {
    // No user is signed in.
  	}
	});
	})

  let balance;
  let numbers;
  let yes = false;
  let questions = [
		{ id: 1, text: `Add Balance` },
		{ id: 2, text: `Withdraw balance` },
	];
	
function addNumber() {
	balance += numbers;
	var sfDocRef = firebase.firestore().collection("users").doc(u);
	return firebase.firestore().runTransaction(function(transaction) {
    return transaction.get(sfDocRef).then(function(sfDoc) {
        if (!sfDoc.exists) {
            throw "Document does not exist!";
        }
		var newBalance = sfDoc.data().balance + numbers;
		if (newBalance >= 0) {
            transaction.update(sfDocRef, { balance: newBalance });
            return newBalance;
        } else {
            return Promise.reject("Transaction Failed");
        }
    });

	}).then(function() {
    	alert("Transaction successfully committed!");
	}).catch(function(error) {
    	alert("Transaction failed: Not Enough balance!", error);
	});
    alert('Balance Added!');
	}

function subNumber() {
	if(balance - numbers >= 0){
		balance -= numbers;
	}
	var sfDocRef = firebase.firestore().collection("users").doc(u);

	return firebase.firestore().runTransaction(function(transaction) {
    return transaction.get(sfDocRef).then(function(sfDoc) {
        if (!sfDoc.exists) {
            throw "Document does not exist!";
        }

		var newBalance = sfDoc.data().balance - numbers;
		if (newBalance >= 0) {
            transaction.update(sfDocRef, { balance: newBalance });
            return newBalance;
        } else {
            return Promise.reject("Transaction Failed");
        }
    });

	}).then(function() {
    alert("Transaction successfully committed!");
	}).catch(function(error) {
    alert("Transaction failed: ", error);
	});
	}



</script>

<style>
	.center{
		align-items: center;
		display: flex;
		flex-direction: column;
	}

  p {
		color: black;
		font-family: 'Arial';
		font-size: 2em;
    align-items: center;
	}
  input { display: block; width: 300px; max-width: 100%;}
  button {
		height: 4rem;
		width: 32rem;
		background-color: black;
		border-color: gray;
		color: white;
		font-size: 2rem;
		background-image: linear-gradient(90deg, white 50%, transparent 50%);
		background-position: 100%;
		background-size: 400%;
	}
	button:hover {
		background-position: 0;
		color:black;
	}
</style>

<div class='center'>
<h1> <title>Balance</title> </h1>
<p> BALANCE = ${balance} </p>

<!-- svelte-ignore a11y-no-onchange -->
<select bind:value={selected} on:change="{() => numbers = ''}">
{#each questions as question}
<option value={question}>
  {question.text}
  </option>
{/each}
</select>

<input type=number bind:value={numbers} min=0 max=1000>
<input type=range bind:value={numbers} min=0 max=1000>

<input type=checkbox bind:checked={yes}> <h6>Check box to continue adding balance.</h6>
{#if yes} <h3>Thank you. Click button to continue.</h3>
{:else} <h3>You must check box to continue.</h3>
{/if} 
{#if selected.id ==1}<button disabled={!yes} on:click|preventDefault={addNumber }>Add ${numbers} to balance</button>
{:else} <button disabled={!yes} on:click|preventDefault={subNumber }>Withdraw ${numbers} from balance</button>
{/if}

</div>