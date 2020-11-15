<script>
    export let portfolio
    import { stores } from '@sapper/app';
    import { onMount } from "svelte";
    const { session } = stores();
    const currencies = []
    onMount(()=>{
        currencies = Object.keys(portfolio)
    })
     

    
</script>
{#each currencies as c}
{portfolio[c]} of {c} {$session.prices[c] * portfolio[c]} 
{/each}