__author__ = 'HP'

""" from numpy import *

print("KAKA")
a = arange(15).reshape(3, 5)
print(a)


import wave
w = wave.open('SignleTone.wav', 'r')
for i in range(w.getnframes()):
    frame = w.readframes(i)
    print(frame)
"""

import wave, struct
from random import randint
waveFile = wave.open('SignleTone.wav', 'r')

length = waveFile.getnframes()
for i in range(0,length):
    waveData = waveFile.readframes(1)
    data = struct.unpack("<h", waveData)
   # print(int(data[0]))
print(length)


noise_output = wave.open('noise.wav', 'w')
noise_output.setparams((2, 2, 44100, 0, 'NONE', 'not compressed'))

for i in range(0, length):
        value = randint(-32767, 32767)
        packed_value = struct.pack('h', value)
        noise_output.writeframes(packed_value)
        noise_output.writeframes(packed_value)

noise_output.close()
