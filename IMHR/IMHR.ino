int pin = 4;
boolean readState = true;
boolean out;
int revCount = 0;

void setup() {
  Serial.begin(9600);
  pinMode(pin, OUTPUT);
  Serial.println("Start");
}                                                                                             

void loop() {
  out = digitalRead(pin);
  if (out and readState)
  {
    revCount++;
    Serial.println(revCount);
    readState = false;
  }
  if (!out)
  {
    readState = true;
  }
}
