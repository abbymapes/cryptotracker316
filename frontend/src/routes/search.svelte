<script>
  import { onMount } from "svelte";
  import Leftbar from "../components/Leftbar.svelte";

  import { stores } from '@sapper/app';
  import firebase from 'firebase/app'
  import 'firebase/firestore'
  const {page,session} = stores();
  const { slug } = $page.params;

  export let currentUsername
  export let falcon = false
  export let loggedIn = false
  let currentUser
  let currentUid

  $: if ($session.ux) {
    currentUsername = $session.ux
    loggedIn = true
  }

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
    const db =  firebase.firestore()
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
                        link: "cryptocurrency"}
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
<body>
<main>
  <div class="menu">
    <Leftbar {falcon} {loggedIn}/>
  </div>
  <div class = "content">
    <div class="search-page">
          <form class="comment-box" name="comment-box" on:submit|preventDefault = {handleSearch}>
            <input type="text" class="search-input" id="search-input" placeholder="Search" bind:value={searchInput} />
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
        <div class = "header">Results</div>
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
  </div>
</main>
</body>

<style>
  /* Results */
  body {
    background-color:black;
  }
  .results {
    align-content: center;
  }
  table {
    padding: 5px;
    background-color: #2A2A2A;
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
      text-align: left;
      text-decoration: none;
  }
  .name-link {
      color: white;
      text-align: center;
      padding-top: 5pt;
      text-decoration: none;
  }
  
  .name-link:hover {
      color: #65ACFF  }
  
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

    }
  
    .search-input {
      font-family: inherit;

    }
  
    input[type="text"] {
      font-family: inherit;
      font-size: 16px;
      text-align: left;
      align-items: center;
      display: flex;
      resize: none;

    }
  
    input {
      font-family: inherit;
      font-size: 18px;
      color: hsl(0, 2%, 30%);
      border-width: 1px;
      border-style: solid;
      border-radius: 10px;
      white-space: nowrap;
      background: white;
    }
  
    input:hover {
      cursor: pointer;
      color: #65ACFF;
      border-color: #65ACFF;
    }
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

  button:focus,
button:active,
button:hover,
input[type="number"]:focus,
select, input[type="text"] 
{
    outline:0px !important;
    -webkit-appearance:none;
    box-shadow: none !important;
}
button ,input[type="number"]{
	background: none;
	color: inherit;
	border: none;

	font: inherit;
    cursor: pointer;

    outline: inherit;

}
input[type="number"]{
	background-color:rgb(77, 77, 77);
}
input[type="text"] ,input,select{
	padding:10px;
	padding-left: 15px;
	padding-right: 15px;
  border: none;
  border-radius: 0px;
}
select{
	background: url('/chevron-down.svg') 96% / 15% no-repeat #EEE;
  width: 15%;
}
input[type="text"] {
  width: 70%;
  border-radius: 25px 0px 0px 25px;
}


input[type="submit"]{
	width: 15%;
  border-radius: 0px 25px 25px 0px;
  transition-duration: .5s;
    background-color: #2E6EFF;
    color: white;
}
input[type="submit"]:hover {
    background-color: #265cdb;
}
  </style>