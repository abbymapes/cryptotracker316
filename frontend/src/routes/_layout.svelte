<script context="module">
    const currencies = ["bitcoin","ethereum","chainlink","litecoin","ripple","dogecoin","bitcoin-cash","binancecoin"]
  
      export async function preload(page, session) {
      session.prices = {}
      let request = this.fetch(`https://api.coingecko.com/api/v3/simple/price?ids=${encodeURIComponent(currencies.join(','))}&vs_currencies=USD`) 
        const res = await (await request).json();
        
       session.prices ={
        BTC : res.bitcoin.usd,
        ETH: res.ethereum.usd,
        LINK : res.chainlink.usd,
        LTC: res.litecoin.usd,
        XRP : res.ripple.usd,
        DOGE :res.dogecoin.usd,
        BCH : res['bitcoin-cash'].usd,
        BNB : res.binancecoin.usd
        }

      return
    } 
  </script>
<script>
    import { onMount } from 'svelte';
    import { stores } from '@sapper/app';
    import Cookies from 'js-cookie';

    import Nav from './../components/Nav.svelte'
    import Leftbar from './../components/Leftbar.svelte'
    import firebase from 'firebase/app'

  import 'firebase/firestore'
	import 'firebase/auth'
    export let falcon = false

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
                    falcon = false;
                    return;
                }
                falcon = true;
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

<slot></slot>

<style>
  /* Container to center page on a screen */
  body {
      background-color: black;
  }
</style>