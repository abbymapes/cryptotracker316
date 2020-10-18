<script context="module">
  const currencies = ["BTC","ETH","LTC"]

	export async function preload(page, session) {
    let ret = {}
    let requests = []
    for(let i = 0 ; i < 3; i++)
      requests = [...requests, this.fetch(`https://api.coinbase.com/v2/prices/${currencies[i]}-USD/spot`)] 
    await Promise.all(requests.map(async r => {
      const res = await (await r).json();
      ret[res.data.base] = res.data.amount
    }))
    return {x:ret}
  }
</script>

<script>
  export let x;
  $: console.log(x)
</script>
<div class="bar">
  {#each currencies as y}
    <span>
      {y} {#if x} ${x[y]} {/if}
    </span>
  {/each}
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

</style>