<script>
import NavBar from './NavBar.svelte';
</script>

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
  text-align: center;
  margin-left: auto;
  margin-right: auto;
  font-family: 'Montserrat';
  font-size: 14pt;
  min-height: 110%;
  background-color: hsl(0, 0%, 98%);
  z-index: -1;
}

.header {
  font-size: 40px;
  color: hsl(210, 35%, 30%);
}
body {
  height: 100%;
  word-break: normal;
}
</style>

  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Balance</title>
    <link rel="stylesheet" href="style.css">
    <link href='https://fonts.googleapis.com/css?family=Montserrat' rel='stylesheet'>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  </head>

<body>
  <div id = "content">
  <NavBar/>
  
  <div class="page-container">
    <div class="center">
      <div class="header">Add Balance</div>
      <!--Content goes here-->
      </div>
    </div>
  </div>
</body>