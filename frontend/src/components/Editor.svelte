<script>

 import { fly } from "svelte/transition";



 export let img
 export let edit 
 export let bio
 export let uid
let files
async function  upload(){
if(files===undefined) return
const st = firebase.storage().ref()
  await st.child(new Date() + '-' + files[0].name).put(files[0])
        .then(snap => snap.ref.getDownloadURL())
        .then(url => img = url)
}
async function update(){

    await firebase.firestore().collection('users').doc(uid).update({
        picture : img,
        bio 
});


}
$: files , upload()

</script>


<div transition:fly={{duration:500,y:50}}>
<h1>Edit Profile</h1>
<div class="image" style={`background-image: url('${img}')`}>
<span class="uplink">
    <input type="file" id="selectedFile" style="display: none;" bind:files />
    <input type="button" value="Upload" onclick="document.getElementById('selectedFile').click();" />
</span>

</div>
<span> Bio: </span>
<textarea bind:value={bio}  rows="4"  />
<span class="close" on:click={()=> edit = !edit}>X</span>

<button on:click={update}> Save </button>
</div>

<style>
div{
    position: fixed; 
    top:40px;
    left:50%;
    transform: translateX(-50%);
    width:400px;
    background: #eaeaea;
    padding: 25px;
    border-radius: 15px;

}
.image{
  width: 200px;
  height: 200px;
    background-position: center;
    background-size: cover;
    background-repeat: no-repeat;
    border-radius: 150px;
    position: relative;
    margin-bottom: 100px;
}
.uplink{

    position: absolute;
    left: 0%;
    top: 0%;
    color: white;
    width: 100%;
    backdrop-filter: brightness(0.8);
    height: 100%;
    display: flex;
    border-radius: 100%;
    align-items: center;
    justify-content: center;
}
textarea{
    width:100%;
    
}
.close{
    position: absolute;
    top:25px;
    right:25px;
}

</style>