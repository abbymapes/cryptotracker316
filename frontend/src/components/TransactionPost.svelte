<script>
  let userLogo = "https://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50";
  let cryptoLogo = "https://s3.amazonaws.com/logos.brandpa.com/uploads/0d56d34d5b9d03d82a25c9e4be00ce89/SuniCoin.png";
  let cryptoName = "SuniCoin";
  let userName = "John Doe";
  let transactionType = "Bought";
  let transactionTime = "5:03pm";
  let transactionDate = "10/4/20";
  let username = "johnDoe";
  let transactionCaption = "Just bought this great new cryptocurrency!";
  let likeStatus = "Like";

</script>

<div class="transaction-post">

	<table class = 'transaction-header'>
		<tr>
			<th class ='transaction-profile-pic'>
				<a href = "/authUser/profile"><img class = "feed-avatar" src = '{userLogo}' alt = 'User Avatar'></a>
			</th>
			<th class ='transaction-name'>
				<a class = "username-link" href = "/authUser/profile">{userName}</a>
			</th>
			<th class = 'transaction-date'>
				{transactionTime}
          <br>
        {transactionDate}
			</th>
		</tr>
	</table>

	<p>{transactionType} <a class = 'crypto-link' href = "/authUser/cryptocurrency">{cryptoName}</a>.</p>
			<a href = "/authUser/cryptocurrency">
				<img src = '{cryptoLogo}' class = 'transaction-logo' alt = 'cryptologo'>
			<br></a>
              
	<p class = 'transaction-caption'> <a class = "username-caption-link" href = "/authUser/profile"><b> @{username}: </b></a>{transactionCaption}</p>

	<table class = 'like-and-comment'>
		<tr>
			<td style = 'width: 25px;'>
				<button class = 'like-button'>{likeStatus}</button>
			</td>
			<td>
				<form class="comment-box" name="comment-box">
			<textarea class="comment-input" id="comment-input" placeholder="Leave a comment"></textarea>
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
    outline-color: hsl(0, 0%, 95%);
    padding: 10px;
  }

  .username-link {
    font-family: inherit;
    color: hsl(210, 35%, 20%);
    text-align: center;
    padding-top: 5pt;
    text-decoration: none;
    font-size: 25px;
  }

  .username-link:hover {
    color: hsl(210, 35%, 50%);
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
  }

  .transaction-caption {
    font-size: 12px;
    text-decoration: none;
  }

  .username-caption-link {
    color: hsl(210, 35%, 20%);
    text-align: center;
    padding-top: 5pt;
    text-decoration: none;
  }

  .username-caption-link:hover {
    color: hsl(210, 35%, 50%);
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
    background-color: rgba(133, 132, 132, 0.356);
  }

  /* Leave a comment box */

  .like-and-comment {
    width: 100%;
    border-collapse: collapse;
    border-spacing: 0;
    text-align: left;
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
    background-color: rgba(133, 132, 132, 0.356);
  }

  img {
    display: block;
    margin-left: auto;
    margin-right: auto;
    height: auto;
    max-width: 70%;
    min-width: 50px;
  }
</style>

