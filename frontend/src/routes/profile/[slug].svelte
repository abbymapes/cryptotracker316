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
    constructor (uid, username, email, balance, picture) {
        this.uid = uid;
        this.username = username;
        this.balance = balance;
        this.email = email;
        this.picture = picture;
    }
    toString() {
        return this.uid + ', ' + this.username + ', ' + this.email, ', ' + this.picture;
    }
}
    import firebase from 'firebase/app'
    import { goto,stores } from '@sapper/app';
    import { onMount, beforeUpdate, afterUpdate } from "svelte";

    const { page} = stores();
    const { slug } = $page.params;
    export let uname = slug
    export let ux = ""
    export let falcon = false
    let loading = true

    $: loading = (posts.count > 0)

    $: if (uname) {
        console.log("Uname changed")
        loading = true
        mount()
    }

    let kaijen 
    let currentUid
    let user
    var followId
    var isFollowed = false

    async function logout() {
        return firebase.auth().signOut().then(() => {
            goto('/login');
        });
    }

    onMount(async()=>{
        mount()
    })


  async function mount() {
    firebase.firestore().collection("users").where("username", "==", uname)
        .get()
        .then(snap=>{
            snap.forEach(doc=>{
                kaijen = JSON.stringify(doc.data())
                user = new User(doc.data().uid, doc.data().username, doc.data().email, doc.data().balance, doc.data().picture)
            })
        }).then(()=> {
            currentUid = firebase.auth().currentUser.uid
        }).then(() => {
            getData();
        })
  }
    
  import TransactionPost from '../../components/TransactionPost.svelte';
  export var posts = [];

  async function getData() {
    const db =  firebase.firestore();
    var userPosts = [];
    db.collection("transaction").where("uid", "==", user.uid).orderBy("time", "desc").get().then(function(snap) {
        snap.forEach(function(item) {
          var transType = 'Bought';
          if (item.data().type == 'sell') {
            transType = 'Sold';
          }
          var date = item.data().time.toDate().toDateString();
          var time = item.data().time.toDate().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
          var u = getUserInfo(db, item.data().uid).then(function(u) {
            var crypto = getCryptoInfo(db, item.data().stock).then(function(crypto) {
              var like = getLikeStatus(db, currentUid, item.data().transid).then(function(like) {
                var count = getLikeCount(db, item.data().transid).then(function(count) {
                  var comments = getComments(db, item.data().transid).then(function(comments) {
                    var commentsWithNames = getUsernames(db, comments).then(function(finalComments) {
                      var follows = getFollowStatus(db, currentUid, user.uid).then(function(follows) {
                        var post = {username: u.uname,
                            transid: item.data().transid,
                            currentUid: user.uid,
                            amount: item.data().amount,
                            userLogo: user.picture,
                            type: transType,
                            date: item.data().time.toDate().toDateString(),
                            time: item.data().time.toDate().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
                            crypto: crypto.name,
                            cryptoPicture: crypto.logo,
                            likeCount: count,
                            caption: item.data().caption,
                            likeStatus: like.status,
                            likeId: like.id,
                            comments: finalComments
                        }
                        console.log("Post: " + post.username + " " + post.caption)
                        userPosts = [...userPosts, post]
                        posts = [...userPosts];
                      })
                    })
                  })
                })
              })
            })
          })
        })
        return userPosts
      })
  }  

  async function getUserInfo(db, uid){
    var user = await db.collection("users").where("uid", "==", uid).get().then(function(snap) {
      snap.forEach(function(item) {
        user = {uname: item.data().username, picture: item.data().picture}
      })
      return user;
    });
    return user;
  }

  async function getLikeCount(db, transid){
    var count = 0;
    var user = await db.collection("likes").where("transid", "==", transid).get().then(function(snap) {
      snap.forEach(function(item) {
        count += 1;
      })
    });
    return count;
  }

  async function getLikeStatus(db, uid, transid){
    var like;
    var user = await db.collection("likes").where("uid", "==", uid).where("transid", "==", transid).get().then(function(snap) {
      snap.forEach(function(item) {
        like = {
          id: item.id,
          status: true
        }
      })
    });
    if (like == null) {
        return {
          id: null,
          status: false
        }
    }
    return like;
  }

  async function getComments(db, transid){
    var comments = await db.collection("comments").where("transid", "==", transid).orderBy("time", "asc").get().then(function(snap) {
      var commentList = [];
      snap.forEach(function(item) {
        var commentToAdd = {
          id: item.id,
          comment: item.data().comment,
          uid: item.data().uid,
          username: ""
        };
        commentList.push(commentToAdd);
        commentList = commentList;
      })
      return commentList
    }).catch(function(error) {
      console.log("Error getting documents: ", error);
    });
    return comments
  }

  async function getUsernames(db, comments) {
    for (var i = 0; i < comments.length; ++i) {
      var comment = comments[i];
      var uname = await db.collection("users").where("uid", "==", comment.uid).get().then(function(snap) {
        var name = "";
        snap.forEach(function(item) {
          name = item.data().username;
        })
        return name;
      })
      comment.username = uname;
      comments[i] = comment;
    }
    return comments
  }

  async function getCryptoInfo(db, stock_symbol) {
    var currency = await db.collection("cryptocurrency").where("stock_symbol", "==", stock_symbol).get().then(function(snap) {
      snap.forEach(function(item) {
        currency = {name: item.data().name, logo: item.data().logo}
      })
      return currency;
    });
    return currency;
  }

  async function getFollowStatus(db, currentUid, otherUid){
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

<head>
    <title>Profile</title>
</head>
<div id = "content">
    <div class="page-container">
      <div class="center">
        <div class="profile-div">
        {#if loading}
            <p> Loading </p>
        {:else}
            <!-- <h1>Hello {uname} {ux} {falcon}</h1> -->
            {#if kaijen}
                <table class = 'profile-header'>
                    <tr>
                        <th class ='profile-pic'>
                            <img class = "profile-avatar" src = '{user.picture}' alt = 'User Profile Picture'>
                        </th>
                        <th class ='profile-name'>
                            <h1>  {uname}</h1>
                        </th>
                        {#if currentUid}
                            {#if user.uid === currentUid}
                                <td class = 'profile-balance'>
                                    Current Balance: ${user.balance}
                                </td>
                            {:else}
                                <td class = 'profile-balance'>
                                    <button class = 'follow-button' on:click = {handleFollow(currentUid, user.uid)}>{(isFollowed) ? 'Unfollow': "Follow"}</button>
                                </td>
                            {/if}
                        {/if}
                    </tr>
                </table>
                
                <div class="header">Transactions</div>
                {#each posts as post}
                    <TransactionPost username = {post.username} userLogo = {post.userLogo} cryptoLogo = {post.cryptoPicture}
                        cryptoName = {post.crypto} transactionType = {post.type} transactionTime = {post.time} isLiked = {post.likeStatus}
                        transactionDate = {post.date} transactionCaption = {post.caption} likeCount = {post.likeCount} amount = {post.amount}
                        currentUid = {post.currentUid} transId = {post.transid} likeId = {post.likeId} comments = {post.comments}/>
                    <br>
                {/each}
            {/if}
        {/if}
        </div>
      </div>
    </div>
  </div>

<style>
    /* Container to center page on a screen */
    .center { grid-area: middle; }
    .page-container{
        grid-template-areas: 'left middle right';
        padding: 10px;
        align-content: center;
        justify-content: center;
        max-width: 80%;
        margin-left: auto;
        margin-right: auto;
    }

    .page-container > div {
        text-align: center;
        padding: 5px 0;
        align-items: center;
    }

    /* Mobile phone constraints */
    @media only screen and (max-width: 670px) {
        .page-container {
        grid-template-areas: 'left middle right';
        padding: 10px;
        align-content: center;
        justify-content: center;
        max-width: 95%;
        margin-left: auto;
        margin-right: auto;
        }
    }
    /* General */
    #content {
        border-bottom: 1px solid rgba(255,62,0,0.1);
        font-weight: 300;
        padding: 0 1em;
        text-align: center;
        margin-left: auto;
        margin-right: auto;
        font-size: 14pt;
        min-height: 110%;
        background-color: hsl(0, 0%, 98%);
        z-index: -1;
    }

    .header {
        font-size: 30px;
        color: hsl(210, 35%, 30%);
    }
    body{
        height: 100%;
        word-break: normal;
    }

    /* Transaction post in feed */
    h1 {
        font-size: 30px;
    }

    .profile-div {
      font-family: inherit;
      margin: auto;
      text-align: center;
      justify-content: center;
      background-color: hsl(0, 0%, 100%);
      outline-color: hsl(0, 0%, 95%);
      padding: 10px;
    }
  
    .profile-avatar {
      border-radius: 50%;
      height: 100px;
      width: 100px;
      vertical-align: middle;
    }

    .profile-balance {
        text-align: right;
        font-family: inherit;
        white-space: nowrap;
    }
  
    .profile-header {
      width: 100%;
    }
  
    .profile-pic {
      width: 100px;
      padding: 10px;
    }
  
    .profile-name {
      width: 100%;
      text-align: left;
    }
  
    /* Follow button */
    .follow-button {
      color: hsl(0, 2%, 30%);
      border-color: hsl(0, 2%, 70%);
      border-width: 1px;
      border-style: solid;
      border-radius: 8px;
      font-family: inherit;
      font-size: 14px;
      white-space: nowrap;
      background: white;
    }
  
    .follow-button:hover {
      cursor: pointer;
      background-color: rgba(133, 132, 132, 0.356);
    }
  
    img {
      display: block;
      margin-left: auto;
      margin-right: auto;
      height: auto;
      max-width: 200px;
      min-width: 50px;
    }
  </style>