<script context="module">
    const currencies = ["BTC","ETH","LTC"]
  
      export async function preload(page, session) {
      session.prices = {}
      let requests = []
      for(let i = 0 ; i < 3; i++)
        requests = [...requests, this.fetch(`https://api.coinbase.com/v2/prices/${currencies[i]}-USD/spot`)] 
      await Promise.all(requests.map(async r => {
        const res = await (await r).json();
        session.prices[res.data.base] = res.data.amount
      }))
      return
    } 
  </script>
<script>
    import { onMount } from 'svelte';
    import { stores } from '@sapper/app';
    import Cookies from 'js-cookie';

    import Nav from './../components/Nav.svelte'

    const { session ,page} = stores();

     onMount(async () => {
            console.log($session.prices)
        firebase.auth().onIdTokenChanged(async (user) => {
            try {
                if (!user) {
                           console.log('User Not Found')
                    Cookies.set('token', false);
                    $session.user = false;
                    $session.ux = false;
                    return;
                }
                const token = await user.getIdToken();
                let uid;
                 await firebase.firestore().collection("users").doc(await user.uid).get().then(async doc=>{
			        if ( doc.exists) 
       	 	       uid = doc.data().username 
    		    })
                $session.user = token;
                $session.ux = uid;
                Cookies.set('token', token);
                console.log($session.ux)
                window.timeoutId = setTimeout(() => {
                    const user = firebase.auth().currentUser;
                    if (user) {
                        return firebase.auth().currentUser.getIdToken(true);
                    }
                  
                }, 1000 * 60 * 55);
            } catch (e) {
                console.log(e);
                Cookies.set('token', false);
                $session.user = false;
                $session.ux = false;
                return;
            }
        });
    });
</script>

{#if $page.error==null}
    <Nav segment = {$page.path}/>
{/if}
	<slot></slot>
