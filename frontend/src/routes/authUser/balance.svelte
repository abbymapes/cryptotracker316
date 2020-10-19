<script>
  let balance = 1000;
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

  p {
		color: black;
		font-family: 'Arial';
		font-size: 2em;
    align-items: center;
	}

  input { display: block; width: 2672px; max-width: 100%;}

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


<h1> <title>Balance</title> </h1>
<p> BALANCE = ${balance} </p>

<select bind:value={selected} on:change="{() => numbers = ''}">
{#each questions as question}
<option value={question}>
      {question.text}
    </option>
  {/each}
</select>

  <input type=number bind:value={numbers} min=0 max=1000>
  <input type=range bind:value={numbers} min=0 max=1000>

    
  <input type=checkbox bind:checked={yes}> Check box to continue adding balance.
    {#if yes}
  <h3>Thank you. Click button to continue.</h3>
    {:else}
  <h3>You must check box to continue.</h3>
    {/if}
  <button disabled={!yes} on:click|preventDefault={addNumber }>Add ${numbers} to balance</button>

