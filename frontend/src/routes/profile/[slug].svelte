<script context="module">
	export async function preload(page, session) {
        const { slug } = page.params;
        let { user,ux } = session;
        let falcon = slug==ux
        console.log(slug)
        console.log(user)
        console.log(ux)
        return {uname : slug, ux, falcon}
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
    export let uname = slug
    export let falcon = false
    export let ux = ""

    let currentUid
    let user
    var followId
    let trades = []
    let edit = false
    var isFollowed = false
    let loading = true

    $: loading = (trades.count > 0)

    $: if (uname) {
        console.log("uname changed " + uname)
        loading = true
        mount()
    }

    async function logout() {
        return firebase.auth().signOut().then(() => {
            goto('/login');
        });
    }

    onMount(async ()=>{
      await mount()
      await getTrades()
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
       }).then(() => {
          getFollowStatus(currentUid, user.uid)
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

  async function getFollowStatus(currentUid, otherUid){
    let db = firebase.firestore()
    var id
    var user = await db.collection("follows").where("uidFollower", "==", currentUid).where("uidFollowing", "==", otherUid).get().then(function(snap) {
      snap.forEach(function(item) {
        isFollowed = true
        followId = item.id
      })
    });
    if (!isFollowed) {
        followId = null
    }
    return id;
  }

  async function handleFollow(currentUid, otherUser) {
    let db = firebase.firestore()
    if (!loading) {
        if (!isFollowed) {
            db.collection("follows").add({
                uidFollower: currentUid,
                uidFollowing: otherUser
            })
            .then(function(docRef) {
                console.log("Follows document written with ID: ", docRef.id);
                followId = docRef.id
            })
            .catch(function(error) {
                console.error("Error adding follows document: ", error);
            });
        } else {
            if (followId) {
                db.collection("follows").doc(followId).delete().then(function() {
                    console.log("Follow document successfully deleted!");
                    followId = null
                }).catch(function(error) {
                    console.error("Error removing document: ", error);
                });
            }
        }
        isFollowed = !isFollowed
    }
  }
  
</script>

<svelte:head>
    <title>Profile</title>
</svelte:head>
<div class="content">
  {#if loading}
    <p> Loading </p>
  {:else}
    {#if user}
      <div>
        <div class="image" style={`background-image: url('${user.picture}')`}></div>
        <h1> {uname}  </h1> 
        <p style="text-align:center">{user.bio}</p>
        {#if falcon}
          <button on:click={logout} > Logout</button>
          <button on:click={()=> edit = !edit} > Edit Profile</button>
          Balance: {user.balance}
        {:else}
          <button class = 'follow-button' on:click = {handleFollow(currentUid, user.uid)}>{(isFollowed) ? 'Unfollow': "Follow"}</button>
        {/if}
      </div>
      <br>

      <div>
      <div class="header"><h1>Trades</h1></div>
      {#if trades}
        {#each trades as trade }
          <Trade {trade} name={user.username} />
        {/each}
      {/if}
      <br>
      </div>
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