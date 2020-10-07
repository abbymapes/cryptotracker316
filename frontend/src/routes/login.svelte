
<script>
    import { goto,stores } from '@sapper/app';
    import firebase from 'firebase/app'
    import {onMount} from 'svelte'

    let email = '';
    let password = '';
    const {session} = stores()
    async function login() {
        firebase.auth().signInWithEmailAndPassword(email, password)
            .then( res => {
                goto('/profile');
            })
            .catch( e =>{
                console.log(e);
            })
    }

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
        firebase.auth().createUserWithEmailAndPassword(email, password)
            .then( res => {
                goto('/profile');
            })
            .catch( e =>{
                console.log(e);
            })
    }



</script>
{#if $session.user}
<button on:click={logout}>Logout</button>    
{:else }

<h1>Login form</h1>

<input type="email" bind:value={email} placeholder="Email" autocomplete="email"/>
<br />

<input type="password" bind:value={password} placeholder="Password" autocomplete="current-password"/>
<br />

<button on:click={login}>Login</button>
<button on:click={signup}>Sign Up</button>
{/if}