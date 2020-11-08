<script>
  
  import { stores } from '@sapper/app';
  import Nav from '../components/Nav.svelte'
  const currencies = ["BTC","ETH","LTC"]
  const { session } = stores();

</script>

<body>
  <Nav/>
</body>

<div class="bar">
  {#each currencies as y}
    <span>
      {y} {#if $session.prices} ${$session.prices[y]} {/if}
    </span>
  {/each}
</div>
<br>
<div class = "name">
  <h1>Aether</h1>
</div>


<style>
.bar{
  background-color: #2A2A2A;
  color: white;
  height: 40px;
  display: flex;
  align-items: center;
  padding:5px;
  justify-content: space-around;
}

h1 {
  background-color: white;
  color: #2A2A2A;
  display: flex;
  align-items: center;
  margin-top: 50px;
  padding:5px;
  justify-content: space-around;
  font-size: 200px;
}

body {
      background-color: black;
  }
  
</style>