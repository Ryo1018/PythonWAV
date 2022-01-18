import sys
import wave
import numpy as np

# 音声ファイル読み込み
in_wav = wave.open(sys.argv[1], "r")

nchannels, sampwidth, framerate, nframes, comptype, compname = in_wav.getparams()
if nchannels != 2:
    print("error: input must stereo.")
    exit()

data = in_wav.readframes(nframes)
tmp_data = np.frombuffer(data, dtype="int16")

# モノラル化
x = tmp_data[::2].copy()

# 出力ファイル書き込み
out_wav = wave.Wave_write(sys.argv[2])
out_wav.setparams((nchannels, sampwidth, framerate, nframes, comptype, compname))
out_wav.writeframes(x)

in_wav.close()
out_wav.close()