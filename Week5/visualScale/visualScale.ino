int potentiometer = 0;
int peopleSwitchPin = 13; 
int difficultySwitchPin = 6; 

#include "HX711.h"
#define calibration_factor -190000.0 //This value is obtained using the SparkFun_HX711_Calibration sketch
#define DOUT  3
#define CLK  2
HX711 scale(DOUT, CLK);



void setup() {
  Serial.begin(9600);

  pinMode(peopleSwitchPin, INPUT);
  pinMode(difficultySwitchPin, INPUT);


  scale.set_scale(calibration_factor); //This value is obtained by using the SparkFun_HX711_Calibration sketch
  scale.tare(); //Assuming there is no weight on the scale at start up, reset the scale to 0


}

void loop() {


  peopleSwitchPin = map(digitalRead(13), 0, 1, 0, 255);
  difficultySwitchPin = map(digitalRead(6), 0, 1, 0, 255);
  potentiometer = map(analogRead(A0), 0, 1023, 0, 255);
  Serial.print(potentiometer);
  Serial.print(",");
  Serial.print(peopleSwitchPin);
  Serial.print(",");
  Serial.print(difficultySwitchPin);
  Serial.print(",");
  Serial.println(scale.get_units(), 1); //scale.get_units() returns a float


  delay(20);
  
 }



 


  
 

