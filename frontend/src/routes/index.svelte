<script>
	import firebase from 'firebase/app';
	import {onMount} from 'svelte';
  import { goto,stores } from '@sapper/app';
  export let segment;

  const {session} = stores()
  let currencies = ["BTC","ETH","LTC"]
  let requests = []
  let x = []
	onMount( async ()=>{
    for(let i = 0 ; i < 3; i++)
      requests = [...requests, fetch(`https://api.coinbase.com/v2/prices/${currencies[i]}-USD/spot`)] 
      let g =  await getData()
      g.forEach(async r=>{
        let re = await r.json()
        console.log(re.data)
        x = [...x,re.data]
      })
      

  })

  async function getData(){
    const res = await Promise.all(requests)
    return res

  }

</script>
<div class="bar">
  {#each currencies as y,i}
    <span>
      {y} {#if x[i]} ${x[i].amount} {/if}
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