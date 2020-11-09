<script>
    import { fly } from "svelte/transition";
    import { onMount } from "svelte";
    import firebase from 'firebase/app'
  import 'firebase/firestore'

    export let toggle
    export let currentUid
    export let postid
    let cuser
    export let comments = []
    let uns = {}
    let commtext = ''
    onMount(async ()=>{
        await unames()
    })
    async  function unames() {
        await comments.forEach(async com => {
            if(uns[com.uid]) return
            await firebase.firestore().collection('users').doc(com.uid).get()
                .then( snapshot => { uns[com.uid] =  snapshot.data()  });
        });
        //console.log( uns )
    }
    async function handleComment() {
        if(commtext=='') {
            alert('Comment can not be empty')
            return
        }

        await firebase.firestore().collection('users').doc(currentUid).get()
            .then(snapshot => { cuser =  snapshot.data()  });
        console.log(await cuser)
        uns[currentUid] = {
            picture : await cuser.picture,
            username : await cuser.username
        }
        comments = [...comments, {
            uid : currentUid,
            comment : commtext
        }] 
        await firebase.firestore().collection('comments').doc().set({
            comment: commtext,
            time: firebase.firestore.FieldValue.serverTimestamp(),
            transid : postid,
            uid : currentUid
        })
    }
</script>


<section transition:fly={{y:-40}}> 
    
    <span class="close" on:click={()=> {toggle = !toggle}}><svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="feather feather-x"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg></span>
    <div  class="comms">
    {#each comments as comment}
        {#if uns[comment.uid]}
            <div class="comment">
                <div>
                    <div class="img" style={`background: url('${uns[comment.uid].picture}');    
                    background-repeat: no-repeat;
                    background-size: cover;
                    background-position: center;
                `}></div>
                </div>
                <div class="body">
                    <h3>  {uns[comment.uid].username} </h3>
                    {comment.comment}
                </div>
            </div>
        {/if}
    {/each}
</div>
<div class="commenter">
    <textarea bind:value={commtext} placeholder="Your Comment"></textarea>
</div>
<button on:click={handleComment} disabled={!currentUid}>
    Add Comment
</button>
</section>

<style>
    section{
        height: calc(100vh - 120px);
    position: fixed;
    width: 80vw;
    max-width: 650px;
    overflow: hidden;

    display: flex;
    flex-direction: column;
    border-radius: 25px;
    min-width: 550px;
    left: 50%;
    z-index: 10;
    background-color: rgb(51, 51, 51);
    color: white;
    top: 50%;
    transform: translate3d(-50%,-50%,0px);

    }
    .close{
        position: absolute;
        top: 20px;
        right: 20px;
    }
    .comment{
        width: 80%;
        display: grid;
        grid-auto-flow: row;
        grid-template-columns: 75px 1fr;
        grid-column-gap: 15px;
        margin-bottom: 35px;
    }
    .img{
        height: 75px;
        width: 75px;
        border-radius: 50%;
    }
    .comms{
        overflow-y: auto;
    box-sizing: border-box;
    height: calc(100% - 200px);
    padding: 25px;

    }
    .commenter {
        position: relative;
        height: 150px;
    }
    .commenter textarea{
        height: 100%;
        width: 100%;
        padding:15px;
        background-color:rgb(77, 77, 77);
    color:white;
    box-sizing: border-box;
    font-family: inherit;
    font-size: 1em;
    }
    textarea:focus{
        
    outline:0px !important;
    -webkit-appearance:none;
    box-shadow: none !important;

    }

    button:focus,
button:active,
button:hover
{
    outline:0px !important;
    -webkit-appearance:none;
    box-shadow: none !important;
}
button {
	background: none;
	color: inherit;
	border: none;
	padding: 0;
	font: inherit;
    cursor: pointer;
    height:50px;
    outline: inherit;
    transition-duration: .5s;
    background-color: #2E6EFF;
    color: white;
}
button:hover {
    background-color: #265cdb;
}
button:disabled{
    color: rgba(255,255,255,.4);
    background-color: #265cdb;
    cursor: not-allowed;
}
</style>