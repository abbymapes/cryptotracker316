<style>
  /* Navigation Bar */
.topnav {
  overflow: hidden;
}

.topnav a {
  float: right;
  display: block;
  color: hsl(210, 35%, 70%);
  text-align: center;
  padding: 15px 15px;
  text-decoration: none;
  font-size: 18px;
}

.topnav a:hover {
  color: hsl(210, 35%, 40%);
}

.topnav a.active {
  float: left;
  color: hsl(210, 35%, 40%);
}

.topnav a.active:hover {
  color: hsl(210, 35%, 70%);
}

.topnav .icon {
  display: none;
}

/* Dropdown menu */
.dropdown {
  float: right;
  overflow: hidden;
}

.dropdown .profile-dropbtn {
  border: none;
  outline: none;
  background-color: inherit;
  font-family: inherit;
  margin: 0;
  float: right;
  display: block;
  color: hsl(210, 35%, 70%);
  text-align: center;
  padding: 15px 15px;
  text-decoration: none;
  font-size: 18px;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

.dropdown-content a {
  float: none;
  text-decoration: none;
  display: block;
  text-align: left;
}

.dropdown-content a:hover {
  background-color: #ddd;
}

.dropdown:hover .dropdown-content {
  display: block;
}

@media screen and (max-width: 670px) {
  .topnav a:not(:first-child) { 
    font-size: 14px;
  }
  .dropdown .profile-dropbtn {
    font-size: 14px;
  }
  .dropdown-content {
    font-size: 14px;
  }
}
</style>

<div class = 'topnav' id = 'myTopNav'>
  <a href="/feed" class="active">CryptoTracker</a>
  <a href="/search">Search</a>
  <a href="/popular">Popular</a>
  <div class = "dropdown">
    <button class="profile-dropbtn">Profile 
      <i class="fa fa-caret-down"></i>
    </button>
    <div class="dropdown-content">
      <a href="/profile">Profile</a>
      <a href="/portfolio">Portfolio</a>
      <a href="/balance">Add Balance</a>
      <a href="/">Logout</a>
    </div>
  </div>
</div>