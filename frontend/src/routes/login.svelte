<script>
    import { goto,stores } from '@sapper/app';
 
    import {onMount} from 'svelte';
    import firebase from 'firebase/app'
  import 'firebase/firestore'
  
  import 'firebase/database'
  
  import 'firebase/auth'


    let email = '';
    let password = '';
    let username = '';
    let first = true;
    let waiting = false;
    let exists = undefined
    const {session,page} = stores()
    async function login() {
        console.log("lo")
        firebase.auth().signInWithEmailAndPassword(email, password)
            .then( res => {
                waiting = true; 
                setTimeout(()=>{
                    goto('/feed');
                },1500)
       
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
                    await firebase.database().ref(`/uids/${res.user.uid}`).set(username)
                    await firebase.firestore().collection('users').doc(res.user.uid).set({
                        uid:res.user.uid,
                        email:res.user.email,
                        createdOn: firebase.firestore.FieldValue.serverTimestamp(),
                        username: username,
                        picture: 'https://www.alliancerehabmed.com/wp-content/uploads/icon-avatar-default.png',
                        balance: 1000
                    })
                    goto(`/profile/${username}`);
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
        //console.log($session.user)
        if ($session.user!='false' && $session.user!=false) {
        
           goto('feed');
        }
    })

$: username , isunique()

    function handleSubmit(){
        console.log('ok')
    }
</script>
<main>
    {#if waiting}
        Waiting...
    {:else}
    <form on:submit|preventDefault="{handleSubmit}" >
        <h1> 
            {#if $page.query.signup}
                Signup
            {:else}
                Login
            {/if} 
        </h1>
        <input type="email" bind:value={email} placeholder="Email" autocomplete="email"/>
        <br />
        <input type="password" bind:value={password} placeholder="Password" autocomplete="current-password"/>
        <br />
        {#if $page.query.signup}
            <input type="username" bind:value={username} placeholder="Username" autocomplete="username"/>
            <b>
                {#if username==''}
                    {" "}
                {:else if  exists==true}
                <svg xmlns="http://www.w3.org/2000/svg" height="30" width="30" viewBox="0 0 24 24" fill="none" stroke="red" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-slash"><circle cx="12" cy="12" r="10"></circle><line x1="4.93" y1="4.93" x2="19.07" y2="19.07"></line></svg>
                {:else if exists==false}
                <svg xmlns="http://www.w3.org/2000/svg" height="30" width="30" viewBox="0 0 24 24" fill="none" stroke="green" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-check"><polyline points="20 6 9 17 4 12"></polyline></svg>
                {:else if exists===undefined}
                <svg xmlns="http://www.w3.org/2000/svg"  height="30" width="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-loader"><line x1="12" y1="2" x2="12" y2="6"></line><line x1="12" y1="18" x2="12" y2="22"></line><line x1="4.93" y1="4.93" x2="7.76" y2="7.76"></line><line x1="16.24" y1="16.24" x2="19.07" y2="19.07"></line><line x1="2" y1="12" x2="6" y2="12"></line><line x1="18" y1="12" x2="22" y2="12"></line><line x1="4.93" y1="19.07" x2="7.76" y2="16.24"></line><line x1="16.24" y1="7.76" x2="19.07" y2="4.93"></line></svg>
                {/if}
            </b>
            <br />
            <button type="submit" on:click={signup} disabled={exists}>Sign Up</button>
        {:else}
            <button type="submit" on:click={login}>Login</button>
        {/if}
        {#if $page.query.signup}
            <a href="/login">  Log In</a>
        {:else}
            <a href="/login?signup=1">  Sign Up </a>
        {/if} 

    </form>
    {/if}
</main>
<style>
main{

    background-color: #121212;
    color: white;
    width: 100vw;
    height:100vh;
}
form{
    position: absolute;
    left: 50%;
    top: 50%;
    border-radius: 15px;
    padding: 50px;
    width: 500px;
    max-width: 500px;
    min-width: 300px;
    background: rgb(50,50,50);
    transform: translate3d(-50%, -50%, 0px);
    text-align: center;
}

input:focus,button:focus,
input:active,button:active,
input:hover,button:hover
{
    outline:0px !important;
    -webkit-appearance:none;
    box-shadow: none !important;
}
input,button {
	background: none;
	color: inherit;
	border: none;
    padding: 10px;
    padding-left: 15px;
    padding-right: 15px;
	font: inherit;
    outline: inherit;
    transition-duration: .5s;
    background-color: rgb(55,55,55);
    color: white;
    width: 100%;
    border-radius: 50px;
    margin-top: 20px;
}
input:hover {
    background-color: rgb(65, 65, 65);
}
button{
    background-color: #2e6dff;
    padding: 10px;
    cursor: pointer;
  height:50px;
}
button:hover {
    background-color: #265cdb;
}
a{
    color: #2e6dff;
    text-decoration: none;
    margin-top: 25px;
    position: absolute;
    transform: translate3d(-50%,190%,0);
    bottom: 0px;
    left: 50%;
}
b{
    margin-top: 20px;
    margin-bottom: -30px;
    display: block;

}
h1{
 
    align-items: center;
    justify-content: flex-end;
    -webkit-user-select: none; /* Chrome/Safari */        
-moz-user-select: none; /* Firefox */
-ms-user-select: none; /* IE10+ */

/* Rules below not implemented in browsers yet */
-o-user-select: none;
user-select: none;
}
</style>