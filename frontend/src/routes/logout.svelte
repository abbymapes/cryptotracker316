<script>
	import { goto,stores } from '@sapper/app';
   
    import {onMount} from 'svelte';

    const {session} = stores()

    onMount(()=>{
        if ($session.user) {
            firebase.auth().signOut()
                .then( res => {
                    goto('login');
                })
                .catch( e =>{
                    console.log(e);
                })
        } else {
            goto('/login');
        }
    });
</script>