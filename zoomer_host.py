# ==================================================
# zoomer_OSUpad v1.0
# Author: Demon King (Король демонов)
# License: GNU GPL v3
# ==================================================
#
# Host script for controlling the Arduino Nano
# that buzzes when Z, X, or Shift are pressed.
# ==================================================

import serial
import time
from pynput import keyboard

PORT = "COM3"  # Change to your COM port
BAUD = 9600

ser = serial.Serial(PORT, BAUD, timeout=0.1)
time.sleep(2)

pressed = set()

def send_signal(sig):
    try:
        ser.write(sig.encode())
    except Exception as e:
        print(f"Serial error: {e}")

def on_press(key):
    try:
        k = key.char.lower()
        if k in ['z', 'x'] and k not in pressed:
            pressed.add(k)
            send_signal(k.upper())
    except AttributeError:
        if key == keyboard.Key.shift and 'shift' not in pressed:
            pressed.add('shift')
            send_signal('S')

def on_release(key):
    try:
        k = key.char.lower()
        if k in pressed:
            pressed.remove(k)
            send_signal('0')
    except AttributeError:
        if key == keyboard.Key.shift and 'shift' in pressed:
            pressed.remove('shift')
            send_signal('0')

print("🔥 zoomer_OSUpad active — press Z/X/Shift to moan.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
