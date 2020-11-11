<script>
    import { stores } from "@sapper/app";
    import { onMount } from "svelte";
    const { page,session} = stores()

    const { slug } = $page.params;
    onMount(()=>{

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
    "hide_side_toolbar": false,
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

{slug}
<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
    <div id="technical-analysis"></div>
    <div class="tradingview-widget-copyright">by TradingView</div>
  </div>
  <!-- TradingView Widget END -->