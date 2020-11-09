import * as sapper from '@sapper/app';
import  firebase from 'firebase/app';


// These imports load individual services into the firebase namespace.


const firebaseConfige = {
	apiKey: "AIzaSyBn1zdf5LjWRSAw0EtkNkErWWURq8F_czU",
	authDomain: "cryptotracker316.firebaseapp.com",
	databaseURL: "https://cryptotracker316.firebaseio.com",
	projectId: "cryptotracker316",
	storageBucket: "cryptotracker316.appspot.com",
	messagingSenderId: "765438654978",
	appId: "1:765438654978:web:0eb4df6fec97e0ccd3051b",
	measurementId: "G-N9G8PYBQSM"
};


firebase.initializeApp(firebaseConfige)

sapper.start({
	target: document.querySelector('#sapper')
});

