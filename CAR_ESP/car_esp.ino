#include "BluetoothSerial.h"

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

BluetoothSerial SerialBT;

int motor1Pin1 = 27; 
int motor1Pin2 = 26; 

int motor1Pin_1 = 32; 
int motor1Pin_2 = 33; 

int enable1Pin1 = 14;
int enable1Pin2 = 25; 

char input;
char data_incom;
// Setting PWM properties
const int freq = 30000;
const int pwmChannel0 = 0;
const int pwmChannel1 = 0;

const int resolution = 8;
int dutyCycle = 200;

void setup() {
  pinMode(motor1Pin1, OUTPUT);
  pinMode(motor1Pin2, OUTPUT);
  pinMode(enable1Pin1, OUTPUT);

  pinMode(motor1Pin_1, OUTPUT);
  pinMode(motor1Pin_2, OUTPUT);
  pinMode(enable1Pin2, OUTPUT);
 
  ledcSetup(pwmChannel0, freq, resolution);
  ledcSetup(pwmChannel1, freq, resolution);
  
  ledcAttachPin(enable1Pin1, pwmChannel0);
  ledcAttachPin(enable1Pin2, pwmChannel1);

  ledcWrite(pwmChannel0, dutyCycle);
  ledcWrite(pwmChannel1, dutyCycle);
  Serial.begin(115200);
  SerialBT.begin();

}

void loop() {
  if (SerialBT.available())
  {
    data_incom = SerialBT.read();
    Serial.println(data_incom);
  }

  if (data_incom == 'F' || data_incom == 'B' || data_incom == 'L' || data_incom == 'R' || data_incom == 'S'){
    input =   data_incom;
  }
  if( input == 'F'){
    forword();
  }else if(input == 'B'){
    backword();
  }else if(input == 'L'){
    left();
  }
  else if(input == 'R'){
    right();
  }else{
    Break();
  }

}

void forword() {
  digitalWrite(motor1Pin_1, HIGH);
  digitalWrite(motor1Pin_2, LOW); 
  digitalWrite(motor1Pin1, LOW);
  digitalWrite(motor1Pin2, HIGH);
  
}

void backword() { 
  digitalWrite(motor1Pin_1, LOW);
  digitalWrite(motor1Pin_2, HIGH); 
  digitalWrite(motor1Pin1, HIGH);
  digitalWrite(motor1Pin2, LOW);
}

void right() {
  digitalWrite(motor1Pin_1, HIGH);
  digitalWrite(motor1Pin_2, LOW); 
  digitalWrite(motor1Pin1, HIGH);
  digitalWrite(motor1Pin2, LOW);
}

void left() {
  digitalWrite(motor1Pin_1, LOW);
  digitalWrite(motor1Pin_2, HIGH); 
  digitalWrite(motor1Pin1, LOW);
  digitalWrite(motor1Pin2, HIGH); 
}

void Break() {
  digitalWrite(motor1Pin_1, LOW);
  digitalWrite(motor1Pin_2, LOW); 
  digitalWrite(motor1Pin1, LOW);
  digitalWrite(motor1Pin2, LOW); 
}
