<script context="module">
	export async function preload(page, session) {
        const { slug } = page.params;
        let { user,ux } = session;
        let falcon = slug==ux

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
    import Post from '../../components/Post.svelte';
    import Editor from '../../components/Editor.svelte';
    import Leftbar from "../../components/Leftbar.svelte";

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
    let post = false
    let comments = []
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
     //     getFollowStatus(currentUid, user.uid)
       })
  }

  async function getTrades() {
    console.log(user.uid)
    await firebase.firestore().collection("transaction").where("uid", "==", user.uid)
        .get()
        .then(snap=>{
            snap.forEach(doc=>{
                trades = [...trades,doc]
                console.log(doc.data().time.seconds)
            })
        })
  }

  async function getFollowStatus(currentUid, otherUid){
    let db = firebase.firestore()
    var id
    await db.collection("follows").where("uidFollower", "==", currentUid).where("uidFollowing", "==", otherUid).get().then(function(snap) {
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
    if (!loading) {
        if (!isFollowed) {
            await firebase.firestore().collection("follows").add({
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
               await firebase.firestore().collection("follows").doc(followId).delete().then(function() {
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
  async function handleViewComment(event) {
    comments = []
    console.log(trades[event.detail.index].id)
    await firebase.firestore().collection("comments").where("transid", "==", trades[event.detail.index].id).orderBy("time","desc").limit(10)
        .get()
        .then(snap=>{
            snap.forEach(doc=>{
              comments = [...comments,doc]
            
                console.log(doc.data())
            })
        })
        .then(e => post = true )
        .catch( e => console.log(e))
  }
  
</script>

<svelte:head>
    <title>{uname} | Profile</title>
</svelte:head>
{#if post}
  <Post comments={comments} bind:toggle={post}/>
{/if}
<main>
  <div class="menu">
    <Leftbar />
  </div>
  <div class="trades">
    <h1>Trades</h1>
    {#if trades}
      {#each trades as trade , index}
        <Trade tradefull={trade} name={user.username} uid={currentUid} {index} on:viewComment={handleViewComment}/>
      {/each}
    {:else}
        Loading
    {/if}
    <br>
  </div>
  <div class="profile">
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

    {/if}
  </div>

</main>



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
main{
  display: grid;
    grid-auto-flow: column;
    grid-template-columns: 80px minmax(300px,550px) 1fr;
    background-color: #121212;
    color: white;
    width: 100vw;
    height:100vh
}
.trades{
  position: relative;
    height: calc(100% - 115px);
    margin-top: 25px;
    border-radius: 25px 25px 0px 0px;
    display: flex;
    background-color: #2A2A2A;
    padding: 45px;
    flex-direction: column;
}
.trades > h1{
  text-align:center;
  margin-bottom: 35px;
  padding-left: 3px;
  letter-spacing: 3px;
  font-weight: 400;
}
  </style>