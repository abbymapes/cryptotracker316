<script>
    import { stores } from "@sapper/app";
    const { page,session} = stores()
    import { onMount } from "svelte";
    const { slug } = $page.params;

    /*
    for given symbol (slug) fetch the price from last x hours (enough to populate chart)
    and then give it to pre built charting library (pancake etc) -- like package in python
    don't worry about style
    */
   //show current price  
   const map = {
       'BTC':'Bitcoin',
       'XRP':'Ripple',
       'LTC':'Litecoin',
       'DOGE':'Dogecoin',
       'ETH':'Ethereum',
       'LINK':'Chainlink',
       'BCH':'Bitcoin Cash',
       'BNB':'Binance Coin'       
   }
   onMount(()=>{
    getTrades()
//     new TradingView.widget(
//     {
//     "width": 980,
//     "height": 610,
//     "symbol": "NASDAQ:AAPL",
//     "interval": "D",
//     "timezone": "Etc/UTC",
//     "theme": "light",
//     "style": "1",
//     "locale": "in",
//     "toolbar_bg": "#f1f3f6",
//     "enable_publishing": false,
//     "allow_symbol_change": true,
//     "container_id": "tradingview_bc973"
//   }
//     );
   })
let trades = []
   async function getTrades() {
    await firebase.firestore().collection("transaction").where("stock", "==", slug.toUpperCase()).limit(5)
        .get()
        .then(snap=>{
            snap.forEach(doc=>{
                trades = [...trades,doc.data()]
                console.log(doc.data())
            })
        })
  }

</script>

<!-- TradingView Widget BEGIN -->
<!-- <div class="tradingview-widget-container">
    <div id="tradingview_bc973"></div>
    <div class="tradingview-widget-copyright"><a href="https://in.tradingview.com/symbols/NASDAQ-AAPL/" rel="noopener" target="_blank"><span class="blue-text">AAPL Chart</span></a> by TradingView</div>
   
  


  </div> -->
  <!-- TradingView Widget END -->



{slug} , {map[slug.toUpperCase()]} ,${$session.prices[slug.toUpperCase()] } , 

{#each trades as trade}
    {JSON.stringify(trade.username)}
{/each}
