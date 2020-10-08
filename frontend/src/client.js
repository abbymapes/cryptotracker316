import * as sapper from '@sapper/app';

import firebase from 'firebase/app';
import "firebase/firestore";
import "firebase/auth";
import 'firebase/database'
// These imports load individual services into the firebase namespace.



// // For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
	apiKey: "AIzaSyBn1zdf5LjWRSAw0EtkNkErWWURq8F_czU",
	authDomain: "cryptotracker316.firebaseapp.com",
	databaseURL: "https://cryptotracker316.firebaseio.com",
	projectId: "cryptotracker316",
	storageBucket: "cryptotracker316.appspot.com",
	messagingSenderId: "765438654978",
	appId: "1:765438654978:web:0eb4df6fec97e0ccd3051b",
	measurementId: "G-N9G8PYBQSM"
  };

let app =firebase.initializeApp(firebaseConfig)
window.db = app.firestore()
window.au = app.auth()


sapper.start({
	target: document.querySelector('#sapper')
});

