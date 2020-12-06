#define SoundSensor 4  //SoundSensor ピン番号
int sensorValue = 0;   //センサの出力値

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}
int i;
void loop() {
  // put your main code here, to run repeatedly:
  int sum=0;
  /*sum = analogRead(SoundSensor);
  delay(1000);*/
  for(i=0;i<60;i++){
    sum += analogRead(SoundSensor);
    delay(1000);
  }
  sum=sum/i;//0秒の平均
  Serial.println(sum);
  
}
