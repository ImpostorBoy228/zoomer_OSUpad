// ==================================================
// zoomer_OSUpad v1.0
// Author: Demon King (Король демонов)
// License: GNU GPL v3
// ==================================================
//
// Description:
// A cursed buzzer-based feedback system for osu!
// Arduino Nano + Python combo that squeals on keypress.
// ==================================================

int buzzerPin = 8;
bool isBeeping = false;

void setup() {
  Serial.begin(9600);
  pinMode(buzzerPin, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    char c = Serial.read();

    switch (c) {
      case 'Z':
        tone(buzzerPin, 880);  // mid tone
        isBeeping = true;
        break;
      case 'X':
        tone(buzzerPin, 1200); // high tone
        isBeeping = true;
        break;
      case 'S':
        tone(buzzerPin, 640);  // low tone (Shift)
        isBeeping = true;
        break;
      case '0': // stop
        if (isBeeping) {
          noTone(buzzerPin);
          isBeeping = false;
        }
        break;
    }
  }
}
