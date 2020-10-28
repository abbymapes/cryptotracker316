<script context="module">
    import {firestore,auth} from './../firebase'
	export async function preload(page, session) {
        let { user } = session;
        if (!user) {
            return this.redirect(302, '/login');
        }
        let au = await auth();
        let dbx = await firestore();
        let u =  au.currentUser
        let n =''
        if(u){
            await dbx.collection("users").doc(u.uid).get().then(async doc=>{
			    if ( doc.exists) 
       	 	       n = doc.data().username 
    		})
        }
        return {uname : n}
    }
</script>
<script>
    import firebase from 'firebase/app'
    import { goto } from '@sapper/app';
    export let uname
    console.log(uname)
    async function logout() {
        return firebase.auth().signOut().then(() => {
            goto('/login');
        });
    }
</script>

<h1>Hello {uname}</h1> 

<button on:click={logout}>Logout</button>