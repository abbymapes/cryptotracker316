<script>
	import { goto,stores } from '@sapper/app';
   
    import {onMount} from 'svelte';
    import firebase from 'firebase/app'
  import 'firebase/auth'
    const {session} = stores()

    onMount(()=>{
        if ($session.user) {
            firebase.auth().signOut()
                .then( res => {
                    goto('/');
                })
                .catch( e =>{
                    console.log(e);
                })
        } else {
            goto('/');
        }
    });
</script>