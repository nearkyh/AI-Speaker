# -*- coding:utf-8 -*-

import os

from utils import recorder
from utils import aibril_module
from utils import speech_to_text
from utils import text_to_speech
from utils import audio_converter
from utils import media_player


if __name__ == '__main__':
    aibril_conn = aibril_module.WatsonServer()
    stt_conn = speech_to_text.SpeechToText()
    tts_conn = text_to_speech.TextToSpeech()

    # while True:
    recording_file = recorder.start_record()

    transcript = stt_conn.audio_stt(recording_file)

    answer = aibril_conn.aibril_conv(transcript)

    # output_gtts = tts_conn.google_tts(answer)
    # output_ntts = tts_conn.naver_tts(answer)
    output_atts = tts_conn.aws_tts(answer)

    # convert_audio = audio_converter.convert(output_gtts)
    # convert_audio = audio_converter.convert(output_ntts)
    convert_audio = audio_converter.convert(output_atts)

    os.system('aplay ' + convert_audio)

    mp = media_player.media_player(transcript)
    print(mp)
    try:
        if mp[-3:] == 'mp3':
            convert_audio = audio_converter.convert(mp)
            os.system('aplay ' + convert_audio + ' &')
        else:
            pass
    except Exception as e:
        pass
