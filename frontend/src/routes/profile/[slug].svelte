<script context="module">



	export async function preload(page, session) {
        const { slug } = page.params;
        let { user,ux } = session;


        return {uname : slug, ux}
    }
</script>
<script>
    import firebase from 'firebase/app'
    import { goto } from '@sapper/app';
    import { onMount } from "svelte";
    export let uname
    export let ux
    let kaijen 
    async function logout() {
        return firebase.auth().signOut().then(() => {
            goto('/login');
        });
    }
    onMount(async()=>{
        console.log(ux)
        firebase.firestore().collection("users").where("username", "==", ux)
        .get()
        .then( snap=>{
            snap.forEach(doc=>{
                kaijen = doc.data().balance
            })
        })
    })
</script>


<h1>Hello {uname} </h1> 
{#if kaijen}
    {kaijen}
{/if}
<button on:click={logout}>Logout</button>