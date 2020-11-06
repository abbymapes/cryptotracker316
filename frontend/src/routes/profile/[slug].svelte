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
    let postid
    let comments = []
    $: loading = (trades.count > 0)

    $: if(uname) updater() 
    async function updater() {
       console.log("uname changed " + uname)
        loading = true
        await mount()
       await  getTrades()
    }

    async function logout() {
        return firebase.auth().signOut().then(() => {
            goto('/login');
        });
    }

    onMount(async ()=>{
      // await mount()
      // await getTrades()
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
         //  console.log(currentUid, user)
       }).then(() => {
          getFollowStatus(currentUid, user.uid)
       })
  }

  async function getTrades() {
   // console.log(user.uid)
   trades = []
    await firebase.firestore().collection("transaction").where("uid", "==", user.uid).orderBy('time').limit(10)
        .get()
        .then(snap=>{
            snap.forEach(doc=>{
                trades = [...trades,doc]
             //   console.log(doc.data().time.seconds)
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
               // console.log("Follows document written with ID: ", docRef.id);
                followId = docRef.id
            })
            .catch(function(error) {
                console.error("Error adding follows document: ", error);
            });
        } else {
            if (followId) {
               await firebase.firestore().collection("follows").doc(followId).delete().then(function() {
                //    console.log("Follow document successfully deleted!");
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
    postid = trades[event.detail.index].id
    await firebase.firestore().collection("comments").where("transid", "==", trades[event.detail.index].id).orderBy("time")
        .get()
        .then(snap=>{
            snap.forEach(doc=>{
              comments = [...comments,doc.data()]
            
                //console.log(doc.data())
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
  <Post comments={comments} bind:toggle={post} {currentUid} {postid}/>
{/if}
<main>
  <div class="menu">
    <Leftbar {falcon}/>
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
    {#if falcon}
    <div class="editbtn" on:click={()=> edit = !edit} > 
      <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="feather feather-edit-2"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"></path></svg>
    </div>
    {/if}
    {#if user}
      <div class="profileinner">
        <div class="image" style={`background-image: url('${user.picture}')`}></div>
        <div class="profileinfo">
          <h1 class="uname"> {uname}  </h1> 
          <div class="ubio">{user.bio}</div>
        </div>
      </div>
      <br>
      <div class="status"> 
      {#if falcon}
      <b>Availiable Balance: <br> ${user.balance}</b>
    {:else}
      <button class = 'follow-button' on:click = {handleFollow(currentUid, user.uid)}>{(isFollowed) ? 'Unfollow': "Follow"}</button>
    {/if}
  </div>
    {/if}
  </div>

</main>



{#if edit}
  <Editor img={user.picture} bio={user.bio} bind:edit uid={user.uid}/>
{/if}

<style>
  .editbtn{
    position: absolute;
    top: 25px;
    right: 0px;
    background: rgba(255, 255, 255, .2);
    padding: 10px;
    display: flex;
    padding-left: 20px;
    padding-right: 25px;
    border-radius: 25px 0px 0px 25px;
    color:#65ACFF;
  }
  .editbtn:hover{
    cursor: pointer;
  }
.image{
  width: 200px;
  height: 200px;
    background-position: center;
    background-size: cover;
    background-repeat: no-repeat;
    border-radius: 150px;

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
.profile{
  padding: 25px;
}
.uname{
  letter-spacing: 5px;
    font-weight: 300;
    font-size: 2.3em;
}
.profileinner{
  display: grid;
  padding-top: 25px;
  grid-auto-flow: column;
    align-items: center;
}
.profileinfo{
  padding:25px;
}
.ubio{
  padding-left: 5px;
  padding-right: 5px;
  color: rgba(255,255,255,.7);
}

button:focus,
button:active,
button:hover
{
    outline:0px !important;
    -webkit-appearance:none;
    box-shadow: none !important;
}
button {
	background: none;
	color: inherit;
	border: none;
  padding: 10px;
  padding-right: 15px;
  padding-left: 15px;
	font: inherit;
    cursor: pointer;
border-radius: 50px;
    outline: inherit;
    transition-duration: .5s;
    background-color: #2E6EFF;
    color: white;
}
button:hover {
    background-color: #265cdb;
}
.status{
  display: flex;
  justify-content: center;
}
.status b{
  font-weight: normal;
  color: rgba(255,255,255,.8);
text-align: center;

}
  </style>