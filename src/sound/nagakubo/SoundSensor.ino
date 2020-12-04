/*
引用　https://wiki.seeedstudio.com/Grove-Sound_Sensor/
========================
接続:  - SoundSensor 		- ESP32 CN3(IO4)
*/
#define SoundSensor 4	//SoundSensor ピン番号

int sensorValue = 0; 	//センサの出力値

void setup() 
	Serial.begin(9600);
}

void loop() {

  long sum = 0;
    for(int i=0; i<32; i++)
    {
        sum += analogRead(SoundSensor);
    }
    sum >>= 5;
    Serial.println(sum); //出力確認
    delay(1000);
	
	
}