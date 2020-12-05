#使用デバイス　GROVE　SoundSensor と　esp32
#esp32からの受信　引用https://umiushi.hateblo.jp/entry/2019/12/11/225643
#serial通信で受信し、それをfirestoreに送信

import serial
import numpy as np

import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#シリアル通信
ser = serial.Serial("COM3",9600)
ser.close()
ser.open()

#部屋の位置座標
# #id_1
# x=0
# y=0.5
# #id_2
# x=0
# y=1
# #id_3
x=1
y=1
#Cloud Firestore SDK初期化
cred = credentials.Certificate('htohu-881c2-firebase-adminsdk-m6g1v-607ecca66a.json')
firebase_admin.initialize_app(cred)
    
db = firestore.client()

listdata=[]
listtime=[]
    
while True:
    #sound sensor　データ取得
    data = ser.readline()
    listdata.append(int(data))
    #a= volume.isdigit()
    #print(a)
    print(listdata)
    #タイムスタンプ取得
    now= datetime.datetime.now()
    listtime.append(now)
    #データ''追加
    doc_ref = db.collection(u'sound').document(u'id_3')
    doc_ref.set({
        u'volume': listdata,
        u'time': listtime,
        u'position_x':x,
        u'position_y':y
    })

