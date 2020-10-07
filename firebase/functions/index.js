const functions = require('firebase-functions');
const admin = require('firebase-admin');
admin.initializeApp();

const db = admin.firestore();
// // Create and Deploy Your First Cloud Functions
// // https://firebase.google.com/docs/functions/write-firebase-functions
//
exports.newUser = functions.auth.user().onCreate((user) => {

    db.collection('users').doc(user.uid).set({
        uid:user.uid,
        email:user.email,
        createdOn:admin.firestore.FieldValue.serverTimestamp()
        
    });


  });
  