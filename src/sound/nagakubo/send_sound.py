
import math
import sys
import time
from grove.adc import ADC　
 
import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#音読み込み（sound sensor）
class GroveSoundSensor:
     
    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC()
 
    @property
    def sound(self):
        value = self.adc.read(self.channel)
        return value
 
Grove = GroveSoundSensor
 
 
def main():
    #Cloud Firestore SDK初期化
    cred = credentials.Certificate('htohu-881c2-firebase-adminsdk-m6g1v-607ecca66a.json')
    firebase_admin.initialize_app(cred)
    
    db = firestore.client()
    #センサーからデータ取得
    if len(sys.argv) < 2:
        print('Usage: {} adc_channel'.format(sys.argv[0]))
        sys.exit(1)
 
    sensor = GroveSoundSensor(int(sys.argv[1]))
 
    print('Detecting sound...')
    while True:
         #タイムスタンプ取得
        now= datetime.datetime.now()
        #データ''追加
        doc_ref = db.collection(u'sound').document()
        doc_ref.set({
            u'volume': sensor.sound,
            u'time': str(now)
        })

        #print('Sound value: {0}'.format(sensor.sound))　#画面出力
        time.sleep(1) #1秒間隔で取得
 

if __name__ == '__main__':
    main()


