<script>
    export let trade
    export let name
    let date = trade.time.toDate()
</script>

<div class="card">
<h3>{trade.type.toUpperCase()}</h3>
<h2>{name}</h2>
<h2>{trade.amount} of {trade.stock}</h2>

<span>{date.getDate()}/{date.getMonth()+1}/{date.getFullYear()}</span>
<p>{trade.caption}</p>
<span> Likes:{trade.like_count} <br> Comments:{trade.comment_count || 0}</span>
</div>

<style>
.card{
    background: #eaeaea;
    float: left;
    padding: 20px;
    border-radius: 15px;
}

</style>
