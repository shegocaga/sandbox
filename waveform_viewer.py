# Stolen from: https://www.youtube.com/watch?v=AShHJdSIxkY

import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt

CHUNK = 1024*4
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

print("lolololol")

p = pyaudio.PyAudio()

stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK
)

data = stream.read(CHUNK)
data_int = struct.unpack(str(2 * CHUNK) + 'B', data)
print(data_int)

fig, ax = plt.subplots()

ax.plot(data_int, '-')
plt.show()
