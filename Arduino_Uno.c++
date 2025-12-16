// UART-Based LED Control using Arduino UNO

void setup() {
  Serial.begin(9600);

  pinMode(2, OUTPUT); // Thumb
  pinMode(3, OUTPUT); // Index
  pinMode(4, OUTPUT); // Middle
  pinMode(5, OUTPUT); // Ring
  pinMode(6, OUTPUT); // Pinky

  digitalWrite(2, LOW);
  digitalWrite(3, LOW);
  digitalWrite(4, LOW);
  digitalWrite(5, LOW);
  digitalWrite(6, LOW);
}

void loop() {
  if (Serial.available()) {
    String cmd = Serial.readStringUntil('\n');
    cmd.trim();

    if (cmd == "thumb_on") digitalWrite(2, HIGH);
    else if (cmd == "thumb_off") digitalWrite(2, LOW);

    else if (cmd == "index_on") digitalWrite(3, HIGH);
    else if (cmd == "index_off") digitalWrite(3, LOW);

    else if (cmd == "middle_on") digitalWrite(4, HIGH);
    else if (cmd == "middle_off") digitalWrite(4, LOW);

    else if (cmd == "ring_on") digitalWrite(5, HIGH);
    else if (cmd == "ring_off") digitalWrite(5, LOW);

    else if (cmd == "pinky_on") digitalWrite(6, HIGH);
    else if (cmd == "pinky_off") digitalWrite(6, LOW);

    else if (cmd == "all_down") {
      digitalWrite(2, LOW);
      digitalWrite(3, LOW);
      digitalWrite(4, LOW);
      digitalWrite(5, LOW);
      digitalWrite(6, LOW);
    }
  }
}
