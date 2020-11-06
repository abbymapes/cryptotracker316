



<script>

import { goto,stores } from '@sapper/app';
import { onMount } from "svelte";


const currencies = ["BTC","ETH","LTC"]
const { session } = stores();

let currentUid
onMount(()=>{currentUid = firebase.auth().currentUser ? firebase.auth().currentUser.uid : undefined})

async function trans() {
    // Add a new document in collection "cities"
    currentUid.
    firebase.firestore().collection("transaction").doc().set({
        amount: 1,
        caption: "hello",
        comment_count: 0,
        like_count: 0,
        stock: "BTC",
        time: firebase.firestore.FieldValue.serverTimestamp(),
        type: "buy",
        uid: currentUid

    })
    .then(function() {
        console.log("Document successfully written!");
    })
    .catch(function(error) {
        console.error("Error writing document: ", error);
});

}

</script>



<button on:click={trans}>
    Add Comment
</button>
