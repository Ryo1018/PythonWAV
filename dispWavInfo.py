import sys
import wave

args = sys.argv
name = args[1]
wav = wave.open(name, "r")

nchannels, sampwidth, framerate, nframes, comptype, compname = wav.getparams()

print("チャンネル数:", nchannels)
print("データサイズ:", sampwidth, "[bytes]")
print("サンプリング周波数:", framerate, "[Hz]")
print("サンプリング数:", nframes, "[frames]")

wav.close()