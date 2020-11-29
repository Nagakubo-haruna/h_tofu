#仕様デバイス
#GROVE　SoundSensor と　Raspberry Pi
#音センサデータ取得　引用https://wiki.seeedstudio.com/Grove-Sound_Sensor/

import math
import sys
import time
from grove.adc import ADC　
 
 
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
    if len(sys.argv) < 2:
        print('Usage: {} adc_channel'.format(sys.argv[0]))
        sys.exit(1)
 
    sensor = GroveSoundSensor(int(sys.argv[1]))
 
    print('Detecting sound...')
    while True:
        print('Sound value: {0}'.format(sensor.sound))　#画面出力
        
        time.sleep(60*10) #10分間隔で取得
 
if __name__ == '__main__':
    main()