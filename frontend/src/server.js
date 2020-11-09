import sirv from 'sirv';
import express from 'express';
import compression from 'compression';
import * as sapper from '@sapper/server';
import cookieParser from 'cookie-parser'; 

const { PORT, NODE_ENV } = process.env;
const dev = NODE_ENV === 'development';

const app = express()
	app.use(cookieParser())
	app.use(
		compression({ threshold: 0 }),
		sirv('static', { dev }),
		sapper.middleware(
			{
			session: async (req, res) => { // populates user if it exists
				if (req.cookies.token) {
					return {
						user: req.cookies.token,
						prices: undefined
					};
				}
				return {
					user: undefined,
					prices: undefined
				};
			}
		}
		)
	)
	if(dev){
	app.listen(PORT, err => {
		if (err) console.log('error', err);
	});
	}

	export default app
