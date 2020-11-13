<script>
    import firebase from 'firebase/app'
    import 'firebase/firestore'
    import { stores } from "@sapper/app";
    import { onMount } from "svelte";
    import Trade from '../../components/Trade.svelte';

    const { page,session} = stores()

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

    let trades = []

    async function getTrades() {
   // console.log(user.uid)
   trades = []
    await firebase.firestore().collection("transaction").where("stock", "==", slug.toUpperCase()).limit(5)
        .get()
        .then(snap=>{
            snap.forEach(doc=>{
                trades = [...trades,doc]
             console.log(doc.data())
            })
        })
  }

    const { slug } = $page.params;
    onMount(()=>{
        getTrades()
        new TradingView.widget(
    {
    "container_id": "technical-analysis",
    "width": (window.innerWidth/3) * 2,
    "height": 600,
    "symbol": `${slug}USD`,
    "interval": "D",
    "timezone": "exchange",
    "theme": "dark",
    "style": "1",
    "toolbar_bg": "#f1f3f6",
    "withdateranges": true,
    "hide_side_toolbar": true,
    "allow_symbol_change": true,
    "save_image": false,
    "studies": [
      "ROC@tv-basicstudies",
      "StochasticRSI@tv-basicstudies",
      "MASimple@tv-basicstudies"
    ],
    "show_popup_button": true,
    "popup_width": "1000",
    "popup_height": "650",
    "locale": "in"
    });
    })
</script>

{slug.toUpperCase()} , {map[slug.toUpperCase()]} ,${$session.prices[slug.toUpperCase()] }


<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
    <div id="technical-analysis"></div>
    <div class="tradingview-widget-copyright">by TradingView</div>
  </div>
  <!-- TradingView Widget END -->

  {#each trades as trade, index}
  <Trade tradefull={trade} {index}/>
{/each}