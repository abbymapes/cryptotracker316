<script>
  import TransactionPost from '../../components/TransactionPost.svelte';
  import { onMount } from "svelte";
  

  var searchInput
  var selectedType
  export var results = [];
  var performedQuery 
  $: loading = (results.count == 0)

  $: console.log(results)

  onMount(()=>{
    const db =  firebase.firestore()
    db.collection("test").get().then(snap =>{
        snap.forEach(item=>{
           console.log(item.id, " => ", item.data());
        })
      })
  })

  async function handleSearch(){
    loading = true
    console.log(searchInput)
    console.log(selectedType)
    var resultsFound = [];
    performedQuery = false
    results = await db.collection(selectedType).get().then(snap =>{
        performedQuery = true
        snap.forEach(item=>{
          if (selectedType == 'cryptocurrency') {
            if (item.data().name && item.data().name.toLowerCase().includes(searchInput.toLowerCase())){
              var result = {name: item.data().name,
                        picture: item.data().logo,
                        link: "authUser/cryptocurrency"}
              resultsFound.push(result);
              console.log(result.name)
              resultsFound = resultsFound;
            }
          } else {
            if (item.data().username && item.data().username.toLowerCase().includes(searchInput.toLowerCase())){
              var result = {name: item.data().username,
                        picture: item.data().picture,
                        link: "profile/" + item.data().username}
              resultsFound.push(result);
              console.log(result)
              resultsFound = resultsFound;
            }
          }
        })
        return resultsFound;
      })
    if (results.count > 0) {
      loading = false
    }
    console.log(loading)
  }

</script>

<head>
  <title>Search</title>
</head>
<!--Content goes here-->

<div class="search-page">
  <form class="comment-box" name="comment-box" on:submit|preventDefault = {handleSearch}>
    <textarea class="search-input" id="search-input" placeholder="Search" bind:value = {searchInput}></textarea>
    <select bind:value={selectedType} id="types" name="types">
      <option value="users">for Users</option>
      <option value="cryptocurrency">for Cryptocurrencies</option>
    </select>
    <input type="submit"/>
  </form>
</div>
{#if performedQuery === false}
  <p>Loading</p>
{:else}
  <header>Results</header>
    {#each results as result}
      <table>
        <tr>
          <td class ='results-pic'>
            <a href = "{result.link}"><img class = "results-avatar" src = '{result.picture}' alt = 'Result Logo'></a>
          </td>
          <td class = 'results-name'>
            <p class = 'name'><a class = "name-link" href = "{result.link}">{result.name}</a></p>
          </td>
        </tr>
      </table>
    {/each}
{/if}

<style>
  /* Results */
  table {
    padding: 10px;
    background-color: white;
    width: 100%;
  }
  .results-avatar {
      border-radius: 50%;
      height: 50px;
      width: 50px;
      vertical-align: middle;
  }
  
  .results-pic {
      width: 50px;
      padding: 10px;
  }

  .results-name {
    text-align: left;
  }
  
  .name {
      font-size: 18px;
      text-decoration: none;
  }
  .name-link {
      color: hsl(210, 35%, 40%);
      text-align: center;
      padding-top: 5pt;
      text-decoration: none;
  }
  
  .name-link:hover {
      color: hsl(210, 35%, 70%);
  }
  
    .search-page {
      font-family: inherit;
      margin: auto;
      text-align: left;
      outline-color: hsl(0, 0%, 95%);
      padding: 10px;
    }
  /* Search box */
    select {
      font-family: inherit;
      font-size: 16px;
      text-align: right;
    }
    form {
      display: flex;
      justify-content: left;
    }
  
    .search-input {
      font-family: inherit;
      border-color: hsl(0, 2%, 70%);
    }
  
    textarea {
      font-family: inherit;
      font-size: 16px;
      text-align: left;
      width: 90%;
      height: 25px;
      display: inline-block;
      resize: none;
      border-radius: 3px;
    }
  
    input {
      font-family: inherit;
      font-size: 18px;
      color: hsl(0, 2%, 30%);
      border-color: hsl(0, 2%, 70%);
      border-width: 1px;
      border-style: solid;
      border-radius: 10px;
      white-space: nowrap;
      background: white;
    }
  
    input:hover {
      cursor: pointer;
      border-color: hsl(210, 35%, 70%);
      color: hsl(210, 35%, 70%);
    }
  </style>