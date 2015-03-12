int led = 13;

void setup()
{
  pinMode(led, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  if(Serial.available()) {
    char command = Serial.read();
    if(command == '1'){
      digitalWrite(led, HIGH);
      Serial.println("Light ON");
    }
    else if(command == '0'){
      digitalWrite(led, LOW);
      Serial.println("Light OFF");
    }
  }
}

