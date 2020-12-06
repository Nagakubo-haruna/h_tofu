#define SoundSensor 4  //SoundSensor ピン番号
int sensorValue = 0;   //センサの出力値

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}
int i;
int volume=0;
void loop() {
  // put your main code here, to run repeatedly:
  int sum=0;
  /*volume = analogRead(SoundSensor);
  delay(1000);*/
  for(i=0;i<5;i++){
    sum += analogRead(SoundSensor);
    //Serial.println(sum);
    delay(1000);
  }
  //Serial.println(i);
  sum=sum/i;//5秒の平均
  
  Serial.println(sum);
  sum=0;
}
