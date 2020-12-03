# サーバーにPOST送信
# 引用　http://independence-sys.net/main/?p=3922
# タイムスタンプつきで送る

import requests
import json
 
from datetime import datetime
 
def uploadSensorValues(temp, hum, press):#引数は温度湿度気圧の３つ
 
    url = 'http://yourdomain/subsub/sensvalues.php'
 
    sensorsdata = {'datetime':datetime.now().strftime("%Y/%m/%d %H:%M:%S"),'temp':temp,'hum':hum,'press':press}
 
    print json.dumps(sensorsdata)
 
    headers = {'content-type': 'application/json'}
 
    res = requests.post(url, data=json.dumps(sensorsdata), headers=headers, verify=False)
 
    print res.json()
    pass
 
def main():
 
    uploadSensorValues(21.8, 39.1, 1020)
 
if __name__ == '__main__':
    main()