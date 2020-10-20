<script context="module">



	export async function preload(page, session) {
        const { slug } = page.params;
        let { user,ux } = session;
        let falcon = slug==ux
        return {uname : slug, ux, falcon}
    }
</script>
<script>

    import firebase from 'firebase/app'
    import { goto,stores } from '@sapper/app';
    import { onMount } from "svelte";

    const { page} = stores();
    const { slug } = $page.params;
    export let uname = slug
    export let ux = ""
    export let falcon = false
    let kaijen 
    async function logout() {
        return firebase.auth().signOut().then(() => {
            goto('/login');
        });
    }
    onMount(async()=>{
        console.log(uname)
        firebase.firestore().collection("users").where("username", "==", uname)
        .get()
        .then( snap=>{
            snap.forEach(doc=>{
                kaijen = JSON.stringify( doc.data())
            })
        })
    })
    
</script>


<h1>Hello {uname} {ux} {falcon}</h1> 
{#if kaijen}
    {kaijen}
{/if}
<button on:click={logout}>Logout</button>