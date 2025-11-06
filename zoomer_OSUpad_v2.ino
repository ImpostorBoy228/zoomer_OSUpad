// ==================================================
// zoomer_OSUpad v1.2
// Author: Demon King (Король демонов)
// License: GNU GPL v3
// ==================================================

int buzzerPin = 8;
bool isBeeping = false;
String input = "";

void setup() {
  Serial.begin(9600);
  pinMode(buzzerPin, OUTPUT);
}

void loop() {
  while (Serial.available()) {
    char c = Serial.read();

    if (c == '\n') {
      processCommand(input);
      input = "";
    } else {
      input += c;
    }
  }
}

void processCommand(String cmd) {
  if (cmd.startsWith("F")) {
    int freq = cmd.substring(1).toInt();
    if (freq > 0) {
      tone(buzzerPin, freq);
      isBeeping = true;
    }
  } 
  else if (cmd == "S") {
    noTone(buzzerPin);
    isBeeping = false;
  }
}
