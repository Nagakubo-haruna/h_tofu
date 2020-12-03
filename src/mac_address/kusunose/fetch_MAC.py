import re
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("htohu-881c2-firebase-adminsdk-m6g1v-607ecca66a.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
docs = db.collection('members').stream()
data = []
for doc in docs:
    data.append(doc.to_dict()['addr'])


with open('caughts', 'r') as f:
    reads = f.read()

scan = []
for i  in reads.strip().split('\n'):
    scan.append(re.match('(.*)\((.*)\) at (.*) on (.*)', i).groups()[2])
    
for i in scan:
    if i in data:
        print(f'{i} is in the room!')