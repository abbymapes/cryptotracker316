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
                  
                    Cookies.set('token', false);
                    $session.user = false;
                    return;
                }
                const token = await user.getIdToken();
                $session.user = token;
                Cookies.set('token', token);
                
              
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
                return;
            }
        });
    });
</script>
{#if $page.error==null}
<Nav></Nav>
{/if}
	<slot></slot>
