
# Aether
This is a Server Side Rendered PWA built in Sapper and hosted on Vercel, using Firebase (BaaS).
### Learning Resource and Guides:
- https://sapper.svelte.dev/docs/
- https://svelte.dev/tutorial/basics
- https://firebase.google.com/docs/web/setup
### Initial Setup
This will only be done once initially.
- After pulling, make/switch to your own branch (For team members only):
```bash
 git branch [name]
 git checkout [name]
```	
- Make sure you have `npm` and `node` (12.x) installed. If not, install them from [here](https://nodejs.org/en/download/).
- Make sure you have firebase CLI installed and are logged in:
```bash
 sudo npm install -g firebase-tools
 firebase login
```
### Setup Frontend 
Locally setup and run the Sapper App on port 3000:
```bash
 cd frontend
 npm i
 npm run dev
```
After this on http://localhost:3000/ your app will be live and will reflect live changes as you edit it.

####  Where to code:
Most of your code will just be within the `/frontend/src` directory.
Every `.svelte` file in `routes` corresponds to a page, and in `components` they represent a resuable component ( look at svelte tutorial to learn how to use components , and Sapper docs on how page routing works ). Ignore `nodemodules`. All `.svelte` files are essentailly a superset of HTML but you can add a lot of functionality with the svelte framework. I have already setup Firebase auth and an example with `index.svelte` ,`login.svelte` and `profile.svelte` routes. Use `static` directory to store cacheable assets like stylesheets, images, etc.

### Setup Backend  ( Node / Firebase )
Add/edit firebase functions:
```bash
 cd firebase/functions
 npm i
```
####  Where to code:
All functions' code will live inside `functions/index.js`. I have setup an example function which is called every time a new user signs up, called `newUser`. Refer to firebase functions documentation for other types of triggers and examples. 
####  Deploying functions:
Deploy all functions:
```bash
 firebase deploy
```
Or, selectively deploy functions by names:
```bash
 firebase deploy --only functions:[func1], functions:[func2]
```
### Project deployment:
This project is hosted at https://aether-five.vercel.app.

