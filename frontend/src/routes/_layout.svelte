<script>
    import { onMount } from 'svelte';
    import { stores } from '@sapper/app';
    import Cookies from 'js-cookie';
	import firebase from 'firebase/app'
    import Nav from './../components/Nav.svelte'

    const { session ,page} = stores();

     onMount(async () => {

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
<Nav/>
{/if}
	<slot></slot>
