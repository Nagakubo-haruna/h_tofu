mergeInto(LibraryManager.library, {

  // Initialize Cloud Firestore through Firebase
  // firebase.initializeApp({
  // apiKey: '### FIREBASE API KEY ###',
  // authDomain: '### FIREBASE AUTH DOMAIN ###',
  // projectId: '### CLOUD FIRESTORE PROJECT ID ###'
  // });

  // const admin = require('firebase-admin');
  // var serviceAccount = require("./config/htohu-881c2-firebase-adminsdk-m6g1v-607ecca66a.json");

  admin.initializeApp({
      type: "service_account",
      project_id: "htohu-881c2",
      private_key_id: "607ecca66a4d883733d6263d055e3150ef55ce17",
      private_key: "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQCb4YPw+pizkmnD\nyLPLPMmgiPq9yQF/d136vSAFor3s3AsXmtZk9HdcwykVJBZ2zAb9X9vIk9GXO8bt\nZ3aldDwZbHExfscYVNZ5JM/j05PXZx6JX4aHkbcecgmE173SsNKE6PlXKi6wzaNn\n3BZbU+A0xDrY9kIfzDKxzqO/PoqmwT1Jq7m5WCkQMDhlNSfdqiL8hkt5UZirGFvg\nAyea+iTv6sevc1OeKfrj2Xq+3Be2eYFRH4Ira77psAhZ0qubvAiRFi8kpSywP5Oq\nVPXetQwiAmEUh2mJLkqu63jHIxDiC9LTVIaC9Pa3nZEdtWl4XruqeBNzuy6KPME7\nW9Bhs2WXAgMBAAECggEAHMWQxWtzwP1e0Tjb2sEDFEMESQBvatgc/BlpbjDeLnhl\nAbveI68t0uzgydqp3M6G4cCOQCTslCX/7zTgJOTh7O1jrTeRxw9tsNmXF52nVaRe\ncgu0OJSwQIna8O6jRl7F1KttzmVmTdL+/L4WUFAYe5TWqdI2XUki+EfEWJnSHLoX\ncHFlYyz+v8AhzoOgchX73K0wN9MzesEl7wgueQNsuirK9oZVQ8VCPxsVVL5vNksc\nJWdPdO4Y3JJc1c2xG0FQVM1pSTw/hqTyq27x+c/ddy+TJT4/vK2cF9XjJHhhEhHM\nFWwJdjhFRqAexI9AoZI3Sn9GPg6hr2CIaelGEZbbvQKBgQDNeDs3gNg1c4+S7cQp\nACLtWlGia7/4yFKazupnVZnWdNDYPsMPMkWB3CfMQQkDodzk7L2je04+2LE0WKvp\nt7cldh0iWRqds/YnBHg6XhZRjeWyb8YYk4akqQZWwTRmhbDYRKXb8zm3D0nqmKIB\n3cwA5u7S579v1Q1DCp35CSSt/QKBgQDCN1KGKoYnbLINRMnvPhC6jlJllakA3exk\n4wsRqQvUKqDGBxwj6aS1NdgKiJ9o2Dywsqe2Eh7hWYxsEZrsfkSz6Ln19Ppbn/Pa\n68WywbCCtO9q9QTDfEmYAOwQdfV9XnbDQN+ZEI6jCAHuZYrTBWW6od/xIAWydECb\nllIZnFLMIwKBgQCDFnYRTy6hy3yKLQ+9aMzfyYPTsBLmUkgBZInAK6jeXeDwVfp0\ns4oM87ygX820d4xKsY+7wWuGRRGpZ/kmP4OlbtnflCGbA7nD4uIhuu1aUsF9OjqU\na2q3mu7kYpdf4WOWVxXKYj8sP6DU/1Q9BJim6q7r99b3LmIrp5Zp0B+KsQKBgQCE\n3docJU1f/VGWGEBZ5skFB8bA7nEPQcOuhVEWROLtxDf3IfgTbY0b13k0Q6Fi1cQ3\nUhHAUodDvcJ+UFD/h6ayuf02keEQ+82VMIUwtKdv1B6SuosGvamPTtowrLJEkXKI\nQ4J0scoTKLBBisA9e0zMMGAHEtQy8Ksehekm0jYmpwKBgQCJSF0O1rkTZ/lJ+biV\nuU/aZ9PoMhR6oYzl68tH0prlry9TWZz7+h/emWAt7GDzLkOuQ0MZE7rcx/qIPcww\nVO6bNkGaHYzH/Tqo9jW2wWhQH2h5lCHW2ns2e4kdTibAuUMJDzPiZVWUxu9iCzja\n7I5AyhYOgr55E5hLaOTAh/UeOw==\n-----END PRIVATE KEY-----\n",
      client_email: "firebase-adminsdk-m6g1v@htohu-881c2.iam.gserviceaccount.com",
      client_id: "112859480307870213957",
      auth_uri: "https://accounts.google.com/o/oauth2/auth",
      token_uri: "https://oauth2.googleapis.com/token",
      auth_provider_x509_cert_url: "https://www.googleapis.com/oauth2/v1/certs",
      client_x509_cert_url: "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-m6g1v%40htohu-881c2.iam.gserviceaccount.com"
  });

  var data = {};
  var db = admin.firestore();
  db.collection('users').get()
    .then((snapshot) => {
        snapshot.forEach((doc) => {
            console.log(doc.id, '=>', doc.data());
            data = doc.data()
        });
    })
    .catch((err) => {
        console.log('Error getting documents', err);
    });

  Firestore: function (data){
    // return data
    window.alert('data:' + data);
  },

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

  // WebGLテクスチャのバインド
  BindWebGLTexture: function (texture) {
    GLctx.bindTexture(GLctx.TEXTURE_2D, GL.textures[texture]);
  },
});