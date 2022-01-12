import sys
import wave
import numpy as np

args = sys.argv
name = args[1]
wav = wave.open(name, "r")

nchannels, sampwidth, framerate, nframes, comptype, compname = wav.getparams()

print("チャンネル数:", nchannels)
print("データサイズ:", sampwidth, "[bytes]")
print("サンプリング周波数:", framerate, "[Hz]")
print("サンプリング数:", nframes, "[frames]")

data = wav.readframes(nframes)
wav_data = np.frombuffer(data, dtype="int16")

for n in wav_data:
    print(n)

wav.close()