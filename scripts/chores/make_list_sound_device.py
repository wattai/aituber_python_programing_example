import sounddevice as sd

with open("sound_device.txt", "w", encoding="utf-8") as f:
    f.write(str(sd.query_devices()))
