import wave
import numpy as np

filepath = "C:/wavProgramming/file_import/sample.wav"
wav = wave.open(filepath, 'rb')

wdata = wav.readframes(wav.getnframes())
data = np.frombuffer(wdata, dtype="int16")

print("Sampling rate :", wav.getframerate())

print(data.shape)
print(data)
print(data.dtype)

wav.close()