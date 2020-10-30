<script>
    import { onMount } from 'svelte';
	import firebase from 'firebase/app'


onMount(()=>{
	firebase.auth().onAuthStateChanged(function(user) {
  		if (user) {
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
  let numbers = 500;
  let yes = false;
  let questions = [
		{ id: 1, text: `Add Balance` },
		{ id: 2, text: `Withdraw balance` },
	];
	let selected;
  function addNumber() {
    balance += numbers;
    alert('Balance Added!');
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
{/if} <button disabled={!yes} on:click|preventDefault={addNumber }>Add ${numbers} to balance</button>

</div>