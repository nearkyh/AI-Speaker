# -*- coding:utf-8 -*-

import os

def convert(input_audio):
    # ================ Audio converter =================
    #   - mp3 to wav
    #   - sample rate(22050Hz to 44100Hz)
    #   - channel(mono to stereo)
    # ==================================================
    convert_audio = "convert_audio.wav"
    cmd_convert = "ffmpeg -i {} -ar 44100 -ac 2 -y {}".format(input_audio, convert_audio)
    os.system(cmd_convert)
    print("Convert mp3 to wav")

    return convert_audio
