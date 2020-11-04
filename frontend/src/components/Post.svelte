<script>
    import { fly } from "svelte/transition";
    import { onMount } from "svelte";
    export let toggle
    export let comments = []
    let uns = {}

    onMount(async ()=>{
        await unames()
    })
    async  function unames() {
        await comments.forEach(async com => {
            if(uns[com.data().uid]) return
            await firebase.firestore().collection('users').doc(com.data().uid).get()
                .then( snapshot => { uns[com.data().uid] =  snapshot.data()  });
        });
        console.log( uns )
    }
</script>


<section transition:fly={{y:-40}}> 
    
    <span class="close" on:click={()=> {toggle = !toggle}}><svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="feather feather-x"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg></span>
    <div  class="comms">
    {#each comments as comment}
        {#if uns[comment.data().uid]}
            <div class="comment">
                <div>
                    <div class="img" style={`background: url('${uns[comment.data().uid].picture}');    
                    background-repeat: no-repeat;
                    background-size: cover;
                    background-position: center;
                `}></div>
                </div>
                <div class="body">
                    <h3>  {uns[comment.data().uid].username} </h3>
                    {comment.data().comment}
                </div>
            </div>
        {/if}
    {/each}
</div>

</section>

<style>
    section{
        height: calc(100vh - 90px);
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
    background-color: white;
    color: black;
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
    }
    .img{
        height: 75px;
        width: 75px;
        border-radius: 50%;
    }
    .comms{
        overflow-y: auto;
        background: red;
    height: calc(100% - 200px);
    padding: 25px;

    }
</style>