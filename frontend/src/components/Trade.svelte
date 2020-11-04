<script>
    export let tradefull
    export let index
    export let uid
    let trade = tradefull.data()
    let tradeid = tradefull.id
    export let name
    let liked = false
    import { stores } from '@sapper/app';
    import { onMount,createEventDispatcher } from "svelte"; 

    const dispatch = createEventDispatcher();

    let date = trade.time.toDate()
    const { session } = stores();

    let l = trade.like_count || 0
    let c = trade.comment_count || 0

    onMount(async ()=> {
        if(uid===undefined) return
        await firebase.firestore().collection("likes").where('uid','==',uid).where('transid','==',tradeid).get()
            .then( snap => {
                snap.forEach(doc => liked = true);
            })
    })


    function handleLike(){
        if(uid===undefined) return
        if(liked){
            l--
            firebase.firestore().collection("likes").where('uid','==',uid).where('transid','==',tradeid)
                .get()
                .then( snap => {
                    snap.forEach(doc => doc.ref.delete());
                })
                .catch(function(error) {
                    console.error("Error removing document: ", error);
                })
        } 
        else {
            l++
            firebase.firestore().collection("likes").doc().set({
            transid: tradeid,
            uid
        })
        } 
        liked = !liked
    }
    function handleComment(){
        dispatch('viewComment', {
            index
        });
    }
</script>

<div class="card">
    <div class="left">
        <h3>{trade.type.toUpperCase()}</h3>
    </div>
    <div class="right">
        <h2>{name}</h2>
        <h2>{trade.amount.toLocaleString()} of <b>{trade.stock} </b></h2>
        
        <span class="date">{date.getDate()}/{date.getMonth()+1}/{date.getFullYear()}</span>
        <p>{trade.caption}</p>
        <span class="social"> 
            {l}  
            <svg on:click={handleLike} style="margin-right: 10px;" class:ok={liked} xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor"  stroke-linecap="round" stroke-linejoin="round" class="feather feather-heart"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
            {c}
            <svg on:click={handleComment}  xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" class="feather feather-message-circle"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
       
        </span>
    </div>
</div>

<style>
.card{
    border-radius: 15px;
    color: black;
    width: 100%;
    grid-template-columns: 85px 1fr;
    position: relative;
    box-shadow: 0px 0px 7px 1px #00000041;
    grid-auto-flow: column;
    display: grid;

}
.left{
    display: flex;
    align-items: center;
    width:85px;
    justify-content: center;
    background-color: black;
    color: white;
    font-size: .9em;
    letter-spacing: 2px;
    padding-left: 2px;
    border-radius: 15px 0px 0px 15px;
}
.right{
    padding:15px;
    background: #ffffff;
    border-radius: 0px 15px 15px 0px;
    position: relative;
}
h2 b{
    font-weight: 400;
    color: #3895ff;
}
.date{
    position: absolute;
    top: 15px;
    right: 15px;
    opacity: .5;
}
.social{
    display: flex;
    line-height: 20px;
    align-items: center;
    justify-content: flex-end;
    -webkit-user-select: none; /* Chrome/Safari */        
-moz-user-select: none; /* Firefox */
-ms-user-select: none; /* IE10+ */

/* Rules below not implemented in browsers yet */
-o-user-select: none;
user-select: none;
}
.social > svg{
    margin-left: 5px;
    transition-duration: .3s;
    stroke-width: 1.8
}
.social > svg:hover{
    cursor: pointer;
    stroke-width: 2
} 

.ok{
    fill: red;
    stroke: none;
}


</style>
