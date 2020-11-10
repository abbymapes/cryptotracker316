const CoinMarketCap = require('coinmarketcap-api')
const client = new CoinMarketCap('1297e4f5-5063-4ebf-ab8b-a28b147f3073')

export async function get(request, response) {
    const { symbol } = request.query
    try {
        const quote = await client.getQuotes({ symbol })
        response.json(quote.data[symbol])
    } catch (err) {
        response.status(500).json({ error: err.message })
    }
}