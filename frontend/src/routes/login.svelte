<script>
    import { goto,stores } from '@sapper/app';
    import firebase from 'firebase/app';
    import {onMount} from 'svelte';
    export let segment;

    let email = '';
    let password = '';
    const {session} = stores()

    onMount(() => {
      if ($session.user) {
        goto('/authUser/feed');
      }
    });

    async function login() {
        firebase.auth().signInWithEmailAndPassword(email, password)
            .then( res => {
                goto('authUser/feed');
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
                goto('/authUser/feed');
            })
            .catch( e =>{
                console.log(e);
            })
    }

</script>

<div id = "content"> 
    <div class="page-container">
        <div class="center">
          <div class="header">CryptoCurrency</div>
            {#if $session.user}
              <button on:click={logout}>Logout</button>    
            {:else }
              <h1>Login form</h1>

              <input type="email" bind:value={email} placeholder="Email" autocomplete="email"/>
              <br/>

              <input type="password" bind:value={password} placeholder="Password" autocomplete="current-password"/>
              <br/>

              <button on:click={login}>Login</button>
              <button on:click={signup}>Sign Up</button>
            {/if}
        </div>
    </div>
</div>

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
    border-bottom: 1px solid rgba(255,62,0,0.1);
  font-weight: 300;
  padding: 0 1em;
    text-align: center;
    margin-left: auto;
    margin-right: auto;
    font-size: 14pt;
    min-height: 110%;
    background-color: hsl(0, 0%, 98%);
    z-index: -1;
  }

  .header {
    font-size: 40px;
    color: hsl(210, 35%, 30%);
  }
</style>