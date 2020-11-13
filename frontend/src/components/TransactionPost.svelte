<script>
  import { goto,stores } from '@sapper/app';

  export let username;
  export let userLogo;
  export let cryptoLogo;
  export let cryptoName;
  export let transactionType;
  export let transactionTime;
  export let transactionDate;
  export let transactionCaption;
  export let isLiked = false;
  export let likeId;
  export let likeCount; 
  export let amount;
  export let currentUid;
  export let transId;
  export let comments;
  var commentInput;
  import firebase from 'firebase/app'
  import 'firebase/firestore'

  const map = {
    'Bitcoin': 'BTC',
    'Ripple': 'XRP',
    'Litecoin': 'LTC',
    'Dogecoin': 'DOGE', 
    'Ethereum': 'ETH',
    'Chainlink': 'LINK',
    'Bitcoin Cash': 'BCH',
    'Binance Coin': 'BNB'
  }

  async function handleComment(id) {
    firebase.firestore().collection("comments").add({
        uid: currentUid,
        transid: id,
        comment: commentInput,
        time : firebase.firestore.FieldValue.serverTimestamp()
      })
      .then(function(docRef) {
        console.log("Comment document written with ID: ", docRef.id);
        location.reload();
      })
      .catch(function(error) {
        console.error("Error adding document: ", error);
      });
    return false;
  }

  async function handleLike(id) {
    if (!isLiked) {
      firebase.firestore().collection("likes").add({
        uid: currentUid,
        transid: id
      })
      .then(function(docRef) {
        likeId = docRef.id;
        console.log("Document written with ID: ", docRef.id);
      })
      .catch(function(error) {
        console.error("Error adding document: ", error);
      });
      likeCount += 1;
    } else {
      firebase.firestore().collection("likes").doc(likeId).delete().then(function() {
        console.log("Document successfully deleted!");
      }).catch(function(error) {
          console.error("Error removing document: ", error);
      });
      likeCount -=1;
    }
    isLiked = !isLiked;
  }

</script>

<div class="transaction-post">
  
  <div class="card">
    <div class="left">
      {#if transactionType == "Bought"}
        <h3>BUY</h3>
      {:else}
        <h3>SELL</h3>
      {/if}
    </div>
  
    <div class="right">
      <table class = 'transaction-header'>
        <tr>
          <th class ='transaction-profile-pic'>
            <a href = "profile/{username}"><img class = "feed-avatar" src = '{userLogo}' alt = 'User Avatar'></a>
          </th>
          <td class ='transaction-name'>
            <h2><a class = "username-link" href = "profile/{username}">{username}</a></h2>
          </td>
          <td class = 'transaction-date'>
            {transactionTime}
              <br>
            {transactionDate}
          </td>
        </tr>
      </table>
        {amount} of <a class = 'crypto-link' href = "currencies/{map[cryptoName]}">{cryptoName}</a>
        <a href = "currencies/{map[cryptoName]}">
				  <img src = '{cryptoLogo}' class = 'transaction-logo' alt = 'cryptologo'>
        <br></a>
        <p class = 'transaction-caption'> <a class = "username-caption-link" href = "profile/{username}"> @{username}: </a>{transactionCaption}</p>
        <span class="social"> 
          <p class = 'transaction-caption'>{likeCount}</p>
          {#if currentUid == "NotLoggedIn"}
          <svg style="margin-right: 10px;" class:ok={isLiked == isLiked} xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor"  stroke-linecap="round" stroke-linejoin="round" class="feather feather-heart"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
          {:else}
            <svg on:click={handleLike(transId)} style="margin-right: 10px;" class:ok={isLiked} xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor"  stroke-linecap="round" stroke-linejoin="round" class="feather feather-heart"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
          {/if}
          </span>

        <table class = 'like-and-comment'>
          <tr>
            <td colspan = 2;>
              <p class = "transaction-description">Comments</p>
            </td>
          </tr>
          {#each comments as comment}
            <tr>
              <td colspan = 2;>
                <p class = 'comment'><a class = "username-caption-link" href = "profile/{comment.username}"> @{comment.username}: </a>{comment.comment}</p>
              </td>
            </tr>
          {/each}
          {#if currentUid != "NotLoggedIn"}
            <tr>
              <td>
                <form class="comment-box" name="comment-box" on:submit|preventDefault = {handleComment(transId)}>
                  <textarea class="comment-input" id="comment-input" placeholder="Leave a comment" bind:value = {commentInput}></textarea>
                  <input type="submit"/>
                </form>
              </td>
            </tr>
          {/if}
        </table>

      </div>
  </div>
</div>

<style>
  /* Transaction post in feed */
  .transaction-post {
    font-family: inherit;
    margin: auto;
    text-align: left;
    padding: 10px;
    border-radius: 15px;
    background-color: inherit;
    width: 100%;
    position: relative;
  }

  .username-link {
    color: hsl(210, 35%, 40%);
    text-align: center;
    padding-top: 5pt;
    text-decoration: none;
    font-weight: 400;
  }

  .username-link:hover {
    color: hsl(210, 35%, 70%);
  }

  .transaction-description {
    font-size: 16px;
    text-align: center;
  }

  .crypto-link {
    color: hsl(210, 35%, 40%);
    text-decoration: none;
  }

  .crypto-link:hover {
    color: hsl(210, 35%, 70%);
  }

  .feed-avatar {
    border-radius: 50%;
    height: 50px;
    width: 50px;
    vertical-align: middle;
  }

  .feed-avatar:hover {
    transform: scale(1.1);
  }

  .transaction-header {
    width: 100%;
  }

  .transaction-profile-pic {
    width: 50px;
  }

  .transaction-name {
    width: 100%;
  }

  .transaction-date {
    font-family: inherit;
    text-align: right;
    font-size: 12px;
    color: hsl(210, 35%, 50%);
    white-space: nowrap;
  }

  .transaction-caption {
    font-size: 16px;
    text-decoration: none;
  }

  .comment {
    font-size: 12px;
    text-decoration: none;
  }
  .username-caption-link {
    color: hsl(210, 35%, 40%);
    text-align: center;
    padding-top: 5pt;
    text-decoration: none;
  }

  .username-caption-link:hover {
    color: hsl(210, 35%, 70%);
  }
  .like-button {
    color: hsl(0, 2%, 30%);
    border-color: hsl(0, 2%, 70%);
    border-width: 1px;
    border-style: solid;
    border-radius: 8px;
    font-size: 12px;
    white-space: nowrap;
    background: white;
  }

  .like-button:hover {
    cursor: pointer;
    border-color: hsl(210, 35%, 70%);
    color: hsl(210, 35%, 70%);
  }

  .like-and-comment {
    width: 100%;
    border-collapse: collapse;
    border-spacing: 0;
    text-align: left;
    padding: 0px;
  }

  form {
    display: flex;
    justify-content: left;
  }

  .comment-input {
    font-family: inherit;
    border-color: hsl(0, 0%, 0%);
  }

  textarea {
    font-size: 12px;
    font-family: inherit;
    text-align: left;
    width: 90%;
    height: 20px;
    display: inline-block;
    resize: none;
    border-radius: 3px;
    border-color: hsl(0, 0%, 0%);
  }

  input {
    font-size: 12px;
    color: hsl(0, 2%, 30%);
    border-color: hsl(0, 2%, 70%);
    border-width: 1px;
    border-style: solid;
    border-radius: 8px;
    white-space: nowrap;
    background: white;
  }

  input:hover {
    cursor: pointer;
    border-color: hsl(210, 35%, 70%);
    color: hsl(210, 35%, 70%);
  }

  img {
    display: block;
    margin-left: auto;
    margin-right: auto;
    height: auto;
    max-width: 150px;
    min-width: 50px;
  }

  .card{
    font-family: inherit;
    border-radius: 15px;
    color: black;
    width: 100%;
    grid-template-columns: 85px 1fr;
    position: relative;
    box-shadow: 0px 0px 7px 1px #00000057;
    grid-auto-flow: column;
    display: grid;

}

.left{
    font-family: inherit;
    display: flex;
    align-items: center;
    width:85px;
    justify-content: center;
    background-color: black;
    color: white;
    font-size: .9em;
    letter-spacing: 2px;
    padding-left: 2px;
    border-radius: 15px 0px 0px 15px;
}
.right{
    font-family: inherit;
    padding:15px;
    background: #ffffff;
    border-radius: 0px 15px 15px 0px;
    position: relative;
}
.social{
    display: flex;
    line-height: 20px;
    align-items: center;
    -webkit-user-select: none; /* Chrome/Safari */        
-moz-user-select: none; /* Firefox */
-ms-user-select: none; /* IE10+ */

/* Rules below not implemented in browsers yet */
-o-user-select: none;
user-select: none;
}
.social > svg{
    margin-left: 5px;
    transition-duration: .3s;
    stroke-width: 1.8
}
.social > svg:hover{
    cursor: pointer;
    stroke-width: 2
} 

.ok{
    fill: red;
    stroke: none;
}
</style>

