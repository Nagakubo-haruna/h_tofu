const functions = require('firebase-functions');
const admin = require('firebase-admin');
const express = require('express');

const app = express();
app.get('/timestamp', (request, response) => {

  var firebaseConfig = {
    apiKey: "AIzaSyDn6kj9sdvuoIf-g-Q2S428rIYlR7wTJgw",
    authDomain: "htohu-881c2.firebaseapp.com",
    databaseURL: "https://htohu-881c2.firebaseio.com",
    projectId: "htohu-881c2",
    storageBucket: "htohu-881c2.appspot.com",
    messagingSenderId: "790225564665",
    appId: "1:790225564665:web:e37254d6a36809ff1b4328",
    measurementId: "G-QD0PRFDPV2"
  };

  admin.initializeApp(firebaseConfig);

  // admin.initializeApp({
  //   credential: admin.credential.cert(serviceAccount)
  // });

  var db = admin.firestore();

  db.collection('users').doc('alovelace').set({
    first: 'bbb',
    last: 'Lovelace',
    born: 11111
  })
  .then(function() {
    console.log("Document successfully written!");
  })
  .catch(function(error) {
    console.error("Error writing document: ", error);
  });

  response.send(`${Date.now()}`);
})

exports.app = functions.https.onRequest(app);


// // Create and Deploy Your First Cloud Functions
// // https://firebase.google.com/docs/functions/write-firebase-functions
//
// exports.helloWorld = functions.https.onRequest((request, response) => {
//   functions.logger.info("Hello logs!", {structuredData: true});
//   response.send("Hello from Firebase!");
// });
