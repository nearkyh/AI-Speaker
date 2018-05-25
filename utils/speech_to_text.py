#-*- coding:utf-8 -*-

import speech_recognition as sr

class SpeechToText:
    def __init__(self):
        self.result_audio_stt = ""
        self.result_mic_stt = ""

    def audio_stt(self, filename):
        with sr.AudioFile(filename) as source:
            r = sr.Recognizer()
            audio = r.record(source)
            try:
                self.result_audio_stt = r.recognize_google(audio, show_all=False, language='ko_KR')
            except Exception as e:
                print(e)

        print("USER>>", self.result_audio_stt)

        return self.result_audio_stt

    def mic_stt(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Say something ...')
            audio = r.listen(source)
        try:
            self.result_mic_stt = r.recognize_google(audio, show_all=False, language='ko_KR')
        except LookupError:
            print('Could not understand audio')

        print("USER>>", self.result_mic_stt)

        return self.result_mic_stt
