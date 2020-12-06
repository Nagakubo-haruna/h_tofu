mergeInto(LibraryManager.library, {
  FireStore: function (){
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

    firebase.initializeApp(firebaseConfig);
    data = {};

    var db = firebase.firestore();

    db.collection('sound').get()
    .then(function(snapshot)  {
        snapshot.forEach(function(doc) {
            console.log(doc.id, '=>', doc.data());
            data = doc.data()
            //send

            //console.logconsole.log();
            SendMessage("GameObject", "LoadVolume", data.volume[data.volume.length - 1])
        });
    })
    .catch(function(err)  {
        console.log('Error getting documents', err);
    });
    //return data;
  },

  //追加


  // 関数呼び出し
  Hello: function () {
    window.alert("Hello, world!");
  },
  // 数値型の引数と戻り値
  AddNumbers: function (x, y) {
    return x + y;
  },
  // 数値型以外の型の引数
  PrintFloatArray: function (array, size) {
    for(var i = 0; i < size; i++)
      console.log(HEAPF32[(array >> 2) + i]);
  },
  // 文字列型の引数
  HelloString: function (str) {
    window.alert(Pointer_stringify(str));
  },
  // 文字列の戻り値
  StringReturnValueFunction: function () {
    var returnStr = "bla";
    var bufferSize = lengthBytesUTF8(returnStr) + 1;
    var buffer = _malloc(bufferSize);
    stringToUTF8(returnStr, buffer, bufferSize);
    return buffer;
  },

});