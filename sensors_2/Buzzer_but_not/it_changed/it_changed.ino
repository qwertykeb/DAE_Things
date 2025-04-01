#define TOUCH_PIN A0     // Touch Sensor connected to A0
#define VIBRATION_PIN 4  // Vibration Motor connected to D4
#define MOTION_PIN 2     // Motion Sensor connected to D2
#define SPEAKER_PIN 3    // DFRobot Speaker connected to D3

void setup() {
    pinMode(TOUCH_PIN, INPUT);
    pinMode(VIBRATION_PIN, OUTPUT);
    pinMode(MOTION_PIN, INPUT);
    pinMode(SPEAKER_PIN, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    int touchState = digitalRead(TOUCH_PIN);   // Read the touch sensor
    int motionState = digitalRead(MOTION_PIN); // Read the motion sensor

    // Motion detection and speaker output
    if (motionState == HIGH) {
        Serial.println("Motion detected! Saying 'Hey'");
        tone(SPEAKER_PIN, 440, 200);  // Play a tone at 440 Hz for 200 ms
        delay(200);                   // Short delay to let the tone play
        noTone(SPEAKER_PIN);           // Stop the tone
    } else {
        noTone(SPEAKER_PIN);  // Ensure speaker is off when no motion
    }

    // Touch detection for continuous vibration
    if (touchState == HIGH) {
        Serial.println("Touch detected! Motor ON");
        digitalWrite(VIBRATION_PIN, HIGH);  // Turn on the vibration motor
    } else {
        Serial.println("No touch. Motor OFF");
        digitalWrite(VIBRATION_PIN, LOW);   // Turn off the vibration motor
    }

    delay(100);  // Small delay to stabilize readings
}

