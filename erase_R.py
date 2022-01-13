import sys
import wave
import numpy as np

# 引数の数をチェック
if len(sys.argv) < 3:
    print("usage: <in file> <out file>")
    exit()

# 音声ファイル読み込み
in_wav = wave.open(sys.argv[1], "r")

nchannels, sampwidth, framerate, nframes, comptype, compname = in_wav.getparams()
if nchannels != 2:
    print("error: input must stereo.")
    exit()

data = in_wav.readframes(nframes)
tmp_data = np.frombuffer(data, dtype="int16")
x = np.array(tmp_data)

# 右チャンネル削除
x[1::2] = 0

# 出力ファイル書き込み
out_wav = wave.open(sys.argv[2], "w")
out_wav.setparams((nchannels, sampwidth, framerate, nframes, comptype, compname))
out_wav.writeframes(x)

in_wav.close()
out_wav.close()