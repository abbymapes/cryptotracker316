<script context="module">
	export async function preload(page, session) {
        const { slug } = page.params;
        let { user,ux } = session;
        let falcon = slug==ux
        return { falcon }
    }
</script>
<script>

class User {
    constructor (uid, username, email, balance, picture, bio) {
      this.uid = uid;
      this.username = username;
      this.balance = balance;
      this.email = email;
      this.picture = picture;
      this.bio = bio || ""
    }
  }
 
    import { goto,stores } from '@sapper/app';
    import { onMount } from "svelte";
    import Trade from '../../components/Trade.svelte';
    import Editor from '../../components/Editor.svelte';

    const { page,session} = stores();
    const { slug } = $page.params;
    let uname = slug
    export let falcon = false

    let currentUid
    let user
    let trades = []
    let edit = false

    async function logout() {
        return firebase.auth().signOut().then(() => {
            goto('/login');
        });
    }

    onMount(async ()=>{
      await mount()
     await  getTrades()
    })


  async function mount() {
    await firebase.firestore().collection("users").where("username", "==", uname)
        .get()
        .then(snap=>{
            snap.forEach(doc=>{
                user = new User(doc.data().uid, doc.data().username, doc.data().email, doc.data().balance, doc.data().picture,doc.data().bio)
            })
        }).then(()=> {
            currentUid = firebase.auth().currentUser ? firebase.auth().currentUser.uid : undefined
        })
        .then(() => {
           console.log(currentUid, user)
       })
  }

  async function getTrades() {
    console.log(user.uid)
    await firebase.firestore().collection("transaction").where("uid", "==", user.uid)
        .get()
        .then(snap=>{
            snap.forEach(doc=>{
             // console.log(trades)
                trades = [...trades,doc.data()]
                console.log(doc.data().time.seconds)
            })
        })
  }
  
</script>

<svelte:head>
    <title>Profile</title>
</svelte:head>
<div class="content">
  {#if user}
<h1> {uname}  </h1> 
{#if falcon}
<button on:click={logout} > Logout</button>
<button on:click={()=> edit = !edit} > Edit Profile</button>
Balance: {user.balance}
{/if}
<a href="/profile/johndoe"> l</a>
<div class="image" style={`background-image: url('${user.picture}')`}></div>
<p style="text-align:center">{user.bio}</p>
  <h2>Trades</h2>
  {#if trades}
    {#each trades as trade }
      <Trade {trade} name={user.username} />
    {/each}
  {/if}
{/if}
</div>

{#if edit}
<Editor img={user.picture} bio={user.bio} bind:edit uid={user.uid}/>
{/if}
<style>
.image{
  width: 200px;
  height: 200px;
    background-position: center;
    background-size: cover;
    background-repeat: no-repeat;
    border-radius: 150px;
    margin:auto;
}
.content{
  padding:10px;
}
  </style>