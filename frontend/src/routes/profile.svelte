<script context="module">
    import firebase from 'firebase/app'
    import { goto } from '@sapper/app';
	export async function preload(page, session) {
        let { user } = session;
        if (!user) {
            return this.redirect(302, '/login');
        }
    }
    
    async function logout() {
        return firebase.auth().signOut().then(() => {
            goto('/login');
        });
    }
</script>


<h1>This is our protected dashboard! Only visible when you are logged in with Firebase</h1> 
<button on:click={logout}>Logout</button>