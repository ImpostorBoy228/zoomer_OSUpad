# ==================================================
# zoomer_OSUpad v1.2
# Author: Demon King (Король демонов)
# License: GNU GPL v3
# ==================================================

import serial
import time
from pynput import keyboard

PORT = "COM3"  # поменяй на свой порт
BAUD = 9600

ser = serial.Serial(PORT, BAUD, timeout=0.1)
time.sleep(2)

last_press = 0
x_held = False

def send_freq(freq):
    try:
        msg = f"F{freq}\n"
        ser.write(msg.encode())
    except Exception as e:
        print(f"Serial error: {e}")

def send_stop():
    ser.write(b"S\n")

def on_press(key):
    global last_press, x_held
    try:
        if key.char.lower() == 'x':
            now = time.time()
            interval = now - last_press if last_press > 0 else 0.5
            last_press = now

            # Чем меньше интервал — тем выше частота
            interval = max(0.05, min(interval, 1.0))
            freq = int(400 + (1 / interval) * 300)  # от ~400 до 2500 Гц

            send_freq(freq)
            x_held = True
    except AttributeError:
        pass

def on_release(key):
    global x_held
    try:
        if key.char.lower() == 'x' and x_held:
            send_stop()
            x_held = False
    except AttributeError:
        pass

print("⚡ zoomer_OSUpad v1.2 — frequency now depends on click speed!")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
