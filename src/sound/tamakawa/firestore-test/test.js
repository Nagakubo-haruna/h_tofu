const admin = require('firebase-admin');

var serviceAccount = require("./config/htohu-881c2-firebase-adminsdk-m6g1v-607ecca66a.json");

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount)
});

var db = admin.firestore();

var docRef = db.collection('users').doc('alovelace');

var setAda = docRef.set({
    first: 'Ada',
    last: 'Lovelace',
    born: 1815
});