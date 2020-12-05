import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("htohu-881c2-firebase-adminsdk-m6g1v-607ecca66a.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def load_register():
    docs = db.collection('members').stream()
    data = []
    for doc in docs:
        if 'addr' in doc.to_dict():
            data.append(doc.to_dict()['addr'])
    return data

def load_sound(id_):
    doc = db.collection('sound').document(id_).get().to_dict()
    return doc