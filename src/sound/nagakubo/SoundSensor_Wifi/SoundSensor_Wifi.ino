/*
引用　catch sound sensor values https://wiki.seeedstudio.com/Grove-Sound_Sensor/
     
========================
接続:

- SoundSensor 		- ESP32 CN3(IO4)
*/
#include <driver/adc.h>　//BLEとアナログ入力併用
//bluetooth設定
#include "BluetoothSerial.h"
BluetoothSerial SerialBT;

//#include <WiFi.h>

#define SoundSensor 4	//SoundSensor ピン番号
int sensorValue = 0;   //センサの出力値

/*// WiFi settings
const char SSID[] = "aterm-5476b0-g";    //WifiアクセスポイントのSSID
const char PASSWORD[] = "353014861cd03";   //上記SSIDに接続するパスワード
WiFiServer server(80);
WiFiClient client;
*/
void setup() {
  SerialBT.begin("ESP32");//bluetooth
  /*//AD1の場合
  adc1_config_width(ADC_WIDTH_BIT_12);
  //何ビットのADCを使うか設定する。今回は12bitにします。
  //adc1の場合はこのように使うチャンネル全体の設定をするコマンドが用意されている。
  adc1_config_channel_atten(ADC1_CHANNEL_0, ADC_ATTEN_DB_0);
  //AD1のチャンネルの設定をする。
  //ここでどのチャンネルを使うか、0 V　~xx Vの値で変換するかを設定する。
  //引数は(設定したいGPIO,AD変換する電圧範囲)を示している。
  //ADC_ATTEN_DB_0 -> 0~1.1VでAD変換する
  */
  //AD2の場合
  adc2_config_channel_atten(ADC2_CHANNEL_5, ADC_ATTEN_DB_11);
  //AD2と違い、この設定コマンドしかない。
  // ADC_ATTEN_DB_11 -> 0~3.9VでAD変換する
	/*Serial.begin(9600);
	while (!Serial);

  WiFi.begin(SSID, PASSWORD);
  Serial.print("WiFi connecting");

  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(100);
    
  }*/
  Serial.println(" connected");

  /*server.begin();
  Serial.print("HTTP Server URL: http://");
  Serial.print(WiFi.localIP());
  Serial.println("/");*/
}

void loop() {
  //WiFiClient client = server.available();
  
  int sum;
  /*//AD1の場合
  sum = adc1_get_raw(ADC1_CHANNEL_0);*/
  //AD2の場合
  //注意　AD2はwi-fiを使っていると使えません！！！！
  esp_err_t r = adc2_get_raw(ADC2_CHANNEL_5, ADC_WIDTH_BIT_12, &sum);
  //引数は(どのチャンネルの値を取得するか、その時何ビットでAD変換した結果にするのか、値を代入する変数)を示しています。
  if ( r == ESP_OK ) {//AD1と違い、errorハンドリングがしやすいようになっています。
    printf("%d\n", sum );
  } else if ( r == ESP_ERR_TIMEOUT ) {
    printf("ADC2 used by Wi-Fi.\n");
  }
  sum = analogRead(SoundSensor);
  /*for(int i=0; i<32; i++){
    sum += analogRead(SoundSensor);
    }
    sum >>= 5;*/
    SerialBT.println(sum); //出力確認
    /*client.println(sum);
    client.stop();*/
    delay(1000);
	
}
