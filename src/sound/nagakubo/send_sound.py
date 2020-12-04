import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#Cloud Firestore SDK初期化
cred = credentials.Certificate('htohu-881c2-firebase-adminsdk-m6g1v-607ecca66a.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

#タイムスタンプ取得
now= datetime.datetime.now()
#データ''追加
doc_ref = db.collection(u'sound').document()
doc_ref.set({
    u'volume': 1,
    u'time': str(now)
})