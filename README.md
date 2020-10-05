# Cryptotracker
This is a Server Side Rendered, PWA built in Sapper and hosted on Firebase. 
### Learning Resource and Guides:
- https://sapper.svelte.dev/docs/
- https://svelte.dev/tutorial/basics
- https://firebase.google.com/docs/web/setup

### Initial Setup
This will only be done once initially.
- After pulling, make/switch to your own branch (For team members only):
```bash
	git branch [name]
```	
- Make sure you have firebase CLI installed and are logged in:
```bash
	npm install -g firebase-tools
	firebase login
```
### Setup Frontend 
Locally setup and run the Sapper App on port 3000 by running the following commands:
```bash
	cd functions
	npm install
	npm run dev
```
After this on http://localhost:3000/ your app will be live and will reflect live changes as you edit it.

### Where to code:
Most of your code will just be within the `/functions/src` directory.
Every `.svelte` file in `routes` corresponds to a page, and in `components` they represent a resuable component ( look at svelte tutorial to learn how to use components , and Sapper docs on how page routing works ). Ignore `nodemodules`. All `.svelte` files are essentailly a superset of HTML but you can add a lot of functionality with the svelte framework. I have included a small example of a database read in the `index.svelte` route. 

### Deployment:
This project is hosted at https://cryptotracker316.web.app.

