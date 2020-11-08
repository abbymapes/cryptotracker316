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

location.reload();
}
$: files , upload()

</script>


<div transition:fly={{duration:500,y:50}} class="mandem">
<h1>Edit Profile</h1>
<div class="image" style={`background-image: url('${img}')`}>
<span class="uplink">
    <input type="file" id="selectedFile" style="display: none;" bind:files />
    <input type="button" value="Upload" onclick="document.getElementById('selectedFile').click();" />
</span>

</div>

<textarea bind:value={bio}  rows="4"  />
<span class="close" on:click={()=> edit = !edit}>
    <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="feather feather-x"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
</span>
<div class="btnc">

    <button on:click={update}> Save </button>
</div>

</div>

<style>
.mandem{
    position: fixed; 
    top:50%;
    left:50%;
    transform: translate3d(-50%,-50%,0);
    width: 500px;
    min-width:350px;
   background-color: rgb(51, 51, 51);
   color:white;

    border-radius: 15px;

}
h1{
    padding: 25px;
}
.image{
  width: 200px;
  height: 200px;
    background-position: center;
    background-size: cover;
    background-repeat: no-repeat;
    border-radius: 150px;
    margin: auto;
    position: relative;
    margin-bottom: 35px;

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
    height: 100px;
    background-color:rgb(77, 77, 77);
    color:white;
    font-family: inherit;
    padding:10px;
  
}
.close{
    position: absolute;
    top:25px;
    right:25px;
    cursor: pointer;
}

input:focus,button:focus,
input:active,button:active,
input:hover,button:hover
{
    outline:0px !important;
    -webkit-appearance:none;
    box-shadow: none !important;
}
input,button {
	background: none;
	color: inherit;
	border: none;
    padding: 10px;
    padding-left: 15px;
    padding-right: 15px;
	font: inherit;
    cursor: pointer;
    outline: inherit;
    transition-duration: .5s;
    background-color: #2e6dff63;
    color: white;
    border-radius: 50px;
}
input:hover {
    background-color: #2e6dff9d;
}
button{
    background-color: #2e6dff;
    padding: 10px;
  height:50px;
    width: 100%;

    border-radius: 0px 0px 15px 15px;

}
button:hover {
    background-color: #265cdb;
}
.btnc{
    display: flex;
    justify-content: center;
    position: relative;
}
</style>