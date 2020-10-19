<script>
    import { goto,stores } from '@sapper/app';
    import firebase from 'firebase/app';
    import {onMount} from 'svelte';

    let email = '';
    let password = '';
    let username = '';
    let first = true;
    let waiting = false;
    let exists = undefined
    const {session,page} = stores()
    async function login() {
        firebase.auth().signInWithEmailAndPassword(email, password)
            .then( res => {
                waiting = true; 
                goto('/authUser/feed');
            })
            .catch( e =>{
                console.log(e);
            })
    }

    // test

    async function logout() {
         firebase.auth().signOut()
            .then( res => {
                goto('/login');
            })
            .catch( e =>{
                console.log(e);
            })
         
    }

    async function signup() {
        if(exists==false){
            await firebase.auth().createUserWithEmailAndPassword(email, password)
                .then( async res => {
                    waiting = true;
                    await firebase.database().ref(`/usernames/${username}`).set(res.user.uid)
                    await firebase.firestore().collection('users').doc(res.user.uid).set({
                        uid:res.user.uid,
                        email:res.user.email,
                        createdOn: firebase.firestore.FieldValue.serverTimestamp(),
                        username: username,
                        picture: 'https://www.alliancerehabmed.com/wp-content/uploads/icon-avatar-default.png',
                        balance: 1000
                    })
                    goto('/feed');
                })
                .catch( e =>{
                    console.log(e);
                })
            
        }
    }
    async function isunique() {
        if(first||username=='') return;
        console.log(username)
        exists = undefined
        await firebase.database().ref(`/usernames/${username}`).once('value').then(snap=>{
            if(snap.val()) exists = true
            else exists = false;
        })
        console.log(exists)
    }
    onMount(()=>{
        first = false;

    })

$: username , isunique()

</script>
{#if waiting}
waiting
{:else}
{#if $session.user}
<button on:click={logout}>Logout</button>    
{:else }

    <h1> {#if $page.query.signup}
        Signup
    {:else}
        Login
    {/if}  form</h1>

    <input type="email" bind:value={email} placeholder="Email" autocomplete="email"/>
    <br />

    <input type="password" bind:value={password} placeholder="Password" autocomplete="current-password"/>
    <br />
    {#if $page.query.signup}
        <input type="username" bind:value={username} placeholder="Username" autocomplete="username"/>
        <b>{#if username==''}
            {" "}
        {:else if  exists==true}
            N
        {:else if exists==false}
            Y
        {:else if exists===undefined}
            W
        {/if}</b>
        <br />
        <button on:click={signup} disabled={exists}>Sign Up</button>
    {:else}
        <button on:click={login}>Login</button>
    {/if}

{/if}
{/if}
