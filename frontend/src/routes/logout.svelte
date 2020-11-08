<script>
	import { goto,stores } from '@sapper/app';
   
    import {onMount} from 'svelte';

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