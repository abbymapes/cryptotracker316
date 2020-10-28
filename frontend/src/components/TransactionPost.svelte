<script>
  import { goto,stores } from '@sapper/app';
  import firebase from 'firebase/app';
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

  async function handleComment(id) {
    db.collection("comments").add({
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
      db.collection("likes").add({
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
      db.collection("likes").doc(likeId).delete().then(function() {
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

	<table class = 'transaction-header'>
		<tr>
			<th class ='transaction-profile-pic'>
				<a href = "profile/{username}"><img class = "feed-avatar" src = '{userLogo}' alt = 'User Avatar'></a>
			</th>
			<td class ='transaction-name'>
				<a class = "username-link" href = "profile/{username}">{username}</a>
			</td>
			<td class = 'transaction-date'>
				{transactionTime}
          <br>
        {transactionDate}
			</td>
		</tr>
	</table>

	<p class = "transaction-description">{transactionType} ${amount} of <a class = 'crypto-link' href = "/authUser/cryptocurrency">{cryptoName}</a>.</p>
			<a href = "/authUser/cryptocurrency">
				<img src = '{cryptoLogo}' class = 'transaction-logo' alt = 'cryptologo'>
			<br></a>
              
	<p class = 'transaction-caption'> <a class = "username-caption-link" href = "profile/{username}"> @{username}: </a>{transactionCaption}</p>
  <p class = 'transaction-caption'>{likeCount} likes</p>
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
		<tr>
			<td style = 'width: 25px;'>
				<button class = 'like-button' on:click = {handleLike(transId)}>{(isLiked) ? 'Unlike': "Like"}</button>
			</td>
			<td>
				<form class="comment-box" name="comment-box" on:submit|preventDefault = {handleComment(transId)}>
			    <textarea class="comment-input" id="comment-input" placeholder="Leave a comment" bind:value = {commentInput}></textarea>
				  <input type="submit"/>
				</form>
			</td>
    </tr>
	</table>
</div>

<style>
  /* Transaction post in feed */
  .transaction-post {
    font-family: inherit;
    margin: auto;
    text-align: left;
    background-color: hsl(0, 0%, 100%);
    outline: solid 1px;
    outline-color: hsl(0, 0%, 95%);
    padding: 10px;
    
  }

  .username-link {
    font-family: inherit;
    color: hsl(210, 35%, 40%);
    text-align: center;
    padding-top: 5pt;
    text-decoration: none;
    font-size: 20px;
  }

  .username-link:hover {
    color: hsl(210, 35%, 70%);
  }

  .transaction-description {
    font-size: 16px;
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
    text-align: right;
    font-size: 12px;
    font-family: inherit;
    color: hsl(210, 35%, 50%);
    white-space: nowrap;
  }

  .transaction-caption {
    font-size: 14px;
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

  /* Like button */
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

  /* Leave a comment box */

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
    border-color: hsl(0, 2%, 70%);
  }

  textarea {
    font-size: 12px;
    text-align: left;
    width: 90%;
    height: 20px;
    display: inline-block;
    resize: none;
    border-radius: 3px;
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
    max-width: 200px;
    min-width: 50px;
  }
</style>

