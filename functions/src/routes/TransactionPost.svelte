<style>
/* Transaction post in feed */
.transaction-post {
  margin: auto;
  text-align: left;
  background-color: hsl(0, 0%, 100%);
  outline-color: hsl(0, 0%, 95%);
  padding: 10px;
}

.username-link {
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
  text-decoration: none;
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
  border-color: hsl(0, 2%, 70%);
}

textarea {
  font-size: 12px;
  text-align: left;
  width: 90%;
  height: 20px;
  display: inline-block;
  font-family: 'Montserrat';
  resize: none;
  border-radius: 3px;
}

input {
  font-family: 'Montserrat';
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

<div class="transaction-post">
	<table class = 'transaction-header'>
		<tr>
			<th class ='transaction-profile-pic'>
				<a href = "/profile.html"><img class = "feed-avatar" src = "https://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50" alt = 'Avatar'>					</a>
			</th>
			<th class ='transaction-name'>
				<a class = "username-link" href = "/profile.html">John Doe</a>
			</th>
			<th class = 'transaction-date'>
				5:03pm<br>10/4/20
			</th>
		</tr>
	</table>
	<p>Bought <a class = 'crypto-link' href = "/cryptocurrency.html">SuniCoin</a>.</p>
			<a href = "/cryptocurrency.html">
				<img src = "https://s3.amazonaws.com/logos.brandpa.com/uploads/0d56d34d5b9d03d82a25c9e4be00ce89/SuniCoin.png" class = 'transaction-logo' alt = 'cryptologo'>
			<br></a>
              
	<p class = 'transaction-caption'> <a class = "username-caption-link" href = "/profile.html"><b> @johnDoe: </b></a> Caption about transaction.</p>

	<table class = 'like-and-comment'>
		<tr>
			<td style = 'width: 25px;'>
				<button class = 'like-button'>Like</button>
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


