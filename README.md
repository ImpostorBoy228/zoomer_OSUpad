# zoomer_OSUpad 🎧💦

**An Arduino + Python project that squeals like a cursed anime idol when you play osu!**  
Licensed under **GPL v3** because freedom must scream too 😈

---

## 💡 Overview

Press `Z`, `X`, or `Shift` while playing osu! — your Arduino Nano will emit glorious tones through a buzzer.  
Supports **multitouch** and **real-time** feedback.

---

## ⚙️ Requirements

- Arduino Nano (Uno also works)
- Passive or Active Buzzer
- 220Ω resistor (for safety and tone stability)
- USB connection to PC
- Python 3.9+
- `pynput` → `pip install pynput`
- `pyserial` → `pip install pyserial`

---

## 🧩 Wiring

### 🧠 ASCII Schematic

csharp
Копировать код
      +5V (Arduino)
          |
          |
         [220Ω]
          |
D8 ---------->●-----> + (Buzzer)
-
|
GND (Arduino)

markdown
Копировать код

> Use pin **D8** for the buzzer signal output.  
> The 220Ω resistor limits current and prevents distorted tones.

---

## 🚀 Installation & Usage

1. Flash `arduino/zoomer_OSUpad.ino` to your Arduino.
2. Connect Arduino via USB.
3. Edit `PORT` in `python/zoomer_host.py` to your COM port.
4. Run:
   ```bash
   python zoomer_host.py
Launch osu! and enjoy the moaning madness.

🔥 Features
Real-time response to osu! keypresses

Multikey (Z/X/Shift) support

Distinct tones per key

Easy to extend (add more keys or MIDI mapping)

Open-source under GPLv3

⚠️ Disclaimer
This software is purely for educational and comedic purposes.
Author is not responsible for psychological, acoustic, or spiritual damage caused by overuse.

🧙 Author
👑 Demon King ImpostorBoy
Licensed under GNU General Public License v3 (GPL-3.0)
© 2025, All screams reserved.
---
