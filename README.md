# zoomer_OSUpad v2

**zoomer_OSUpad** is an Arduino + Python project that uses a buzzer to generate tones whose frequency depends on how quickly you press the **X** key.  
The faster you press, the higher the tone.  
Version **v2** introduces real dynamic frequency control and proper long-press handling.

---

## 🚀 What’s New in v2

| Feature | v1 | v2 |
|----------|----|----|
| Key input | Z, X, Shift | Only X |
| Frequency | Fixed per key | Dynamic — depends on click interval |
| Long press support | Partial | Full (tone holds while key is pressed) |
| Communication | Symbol-based | Numeric frequency over serial |
| Accuracy | Basic | High — interval measured on host side |

---

## ⚙️ System Overview

- **Host (Python)**  
  Detects key presses using `pynput`, measures time between clicks, and sends the computed frequency to Arduino via serial.

- **Arduino (C++)**  
  Receives frequency values and generates tone output on a buzzer connected to **D8**.

---

## 🔌 Wiring

### ASCII schematic

      +5V (Arduino)
          |
         [220Ω]
          |
D8 ---------->●-----> + (Buzzer)
-
|
GND (Arduino)

> Use a 220 Ω resistor in series to protect the buzzer and stabilize tone output.

---

## 🎚️ Frequency Mapping

| Click interval (seconds) | Approx. frequency (Hz) | Description |
|---------------------------|------------------------|--------------|
| ≥ 1.0                    | ~400 Hz               | slow press – low tone |
| 0.5                      | ~800 Hz               | medium pace |
| 0.3                      | ~1200 Hz              | moderately fast |
| 0.1                      | ~2500 Hz              | rapid pressing – high tone |
| ≤ 0.05                   | capped at 3000 Hz     | max limit to avoid distortion |

*(Exact curve: `freq = 400 + (1/interval) * 300`, clamped to 3000 Hz.)*

---

## 🧠 Requirements

- Arduino Nano or Uno  
- Passive or active buzzer  
- 220 Ω resistor  
- Python ≥ 3.9  
- Libraries:  
  ```bash
  pip install pyserial pynput
▶️ Usage
Flash arduino/zoomer_OSUpad_v2.ino to your Arduino.

Edit PORT in python/zoomer_host_v2.py to match your COM port.

Run the host script:
python zoomer_host_v2.py
Press or hold the X key — tone frequency changes with your click rhythm.

📜 License
Licensed under GNU GPL v3.
© 2025 Demon King ImpostorBoy
