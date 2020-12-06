import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore, storage

cred = credentials.Certificate("htohu-881c2-firebase-adminsdk-m6g1v-607ecca66a.json")
firebase_admin.initialize_app(cred, {'storageBucket': 'htohu-881c2.appspot.com'})
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

def store_roomdata(dic):
    doc_ref = db.collection('estim').document('room')
    doc_ref.set(dic)

def store_image(path):
    bucket = storage.bucket()

    filename = path
    content_type = 'image/png'
    blob = bucket.blob(filename)
    with open(filename, 'rb') as f:
        blob.upload_from_file(f, content_type=content_type)