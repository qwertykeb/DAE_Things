#define TOUCH_PIN A0     // Touch Sensor connected to A0
#define VIBRATION_PIN 3  // Vibration Motor connected to D3

void setup() {
    pinMode(TOUCH_PIN, INPUT);
    pinMode(VIBRATION_PIN, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    int touchState = digitalRead(TOUCH_PIN);  // Read Touch Sensor

    if (touchState == HIGH) {
        Serial.println("Touch detected! Motor ON");
        digitalWrite(VIBRATION_PIN, HIGH);  // Turn on the vibration motor
    } else {
        Serial.println("No touch. Motor OFF");
        digitalWrite(VIBRATION_PIN, LOW);   // Turn off the vibration motor
    }

    delay(100);  // Small delay to prevent rapid toggling
}
