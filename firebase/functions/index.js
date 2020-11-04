const functions = require('firebase-functions');
const admin = require('firebase-admin');
admin.initializeApp();

const db = admin.firestore();
// // Create and Deploy Your First Cloud Functions
// // https://firebase.google.com/docs/functions/write-firebase-functions
//
exports.newLike = functions.firestore
    .document('likes/{likeId}')
    .onCreate(async (snap, context) => {
      // Get an object representing the document
      // e.g. {'name': 'Marie', 'age': 66}
      const toLike = snap.data().transid
      await db.collection('transaction').doc(toLike)
        .update({
            like_count: admin.firestore.FieldValue.increment(1)
        });
      // perform desired operations ...
    });

exports.delLike = functions.firestore
    .document('likes/{likeId}')
    .onDelete(async (snap, context) => {
      // Get an object representing the document
      // e.g. {'name': 'Marie', 'age': 66}
      const toLike = snap.data().transid
      await db.collection('transaction').doc(toLike)
        .update({
            like_count: admin.firestore.FieldValue.increment(-1)
        });
      // perform desired operations ...
    });