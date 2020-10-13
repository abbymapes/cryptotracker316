<script>
  import TransactionPost from '../../components/TransactionPost.svelte';
  import firebase from 'firebase/app';
  import {onMount} from 'svelte';

  let loading = true;
  const currentUid = 'dyRLLClJ7EQYoGh6qgD12hPCfV92';
  export var posts = [];
  export let followingIds = [];

  onMount(async()=>{
    getData()
    .then(res=>loading = false);
  })

  async function getData() {
    const db =  firebase.firestore();
    var userPosts = [];
    getFollowingUsers(db, currentUid).then(function() {
      db.collection("transaction").where("uid", "in", followingIds).orderBy("time", "desc").get().then(function(snap) {
        snap.forEach(function(item) {
          var transType = 'Bought';
          if (item.data().type == 'sell') {
            transType = 'Sold';
          }
          var date = item.data().time.toDate().toDateString();
          var time = item.data().time.toDate().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
          var user = getUserInfo(db, item.data().uid).then(function(user) {
            var crypto = getCryptoInfo(db, item.data().stock).then(function(crypto) {
              var like = getLikeStatus(db, currentUid, item.data().transid).then(function(like) {
                var count = getLikeCount(db, item.data().transid).then(function(count) {
                  var comments = getComments(db, item.data().transid).then(function(comments) {
                    var commentsWithNames = getUsernames(db, comments).then(function(finalComments) {
                      console.log(finalComments)
                      var post = {username: user.uname,
                        transid: item.data().transid,
                        currentUid: currentUid,
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
                      userPosts = [...userPosts, post]
                      posts = [...userPosts];
                    })
                  })
                })
              })
            })
          })
        })
        return userPosts
      })
    })
  }  

  async function getFollowingUsers(db, uid) {
    var following = await db.collection("follows").where("uidFollower", "==", uid).get().then(function(snap) {
        snap.forEach(function(item) {
          followingIds.push(item.data().uidFollowing);
          followingIds = followingIds;
        });
      }).catch(function(error) {
      console.log("Error getting documents: ", error);
    });
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
        console.log(item.data());
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

</script>

<style>
</style>

<head>
  <title>Feed</title>
</head>

{#if loading}
  <p> Loading </p>
{:else}
  {#each posts as post}
    <TransactionPost username = {post.username} userLogo = {post.userLogo} cryptoLogo = {post.cryptoPicture}
      cryptoName = {post.crypto} transactionType = {post.type} transactionTime = {post.time} isLiked = {post.likeStatus}
      transactionDate = {post.date} transactionCaption = {post.caption} likeCount = {post.likeCount} amount = {post.amount}
      currentUid = {post.currentUid} transId = {post.transid} likeId = {post.likeId} comments = {post.comments}/>
    <br>
  {/each}
{/if}