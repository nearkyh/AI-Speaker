# AI-Speaker
Implemented Artificial Intelligent Speaker.


## Used API
Speech to Text : [Google Streaming Speech Recognition API](https://cloud.google.com/speech/docs/streaming-recognize) \
Conversaion : [Watson](https://console.bluemix.net/docs/services/conversation/getting-started.html#gettingstarted), [Aibril(korean)](https://www.aibril.com/doc/Conversation/010.html)\
Text to Speech : [gTTS](https://pypi.python.org/pypi/gTTS), [Naver Clova TTS](https://developers.naver.com/products/clova/tts/), [AWS Polly TTS](https://github.com/yonghankim/aws-polly)


## Requirements
- Ubuntu 16.04
- Python 3.5


## Dependencies
- `sudo apt-get install python3-dev`
- `sudo apt-get install portaudio19-dev`
- `sudo apt-get install ffmpeg`


## Setting Environment
Google Streaming Speech Recognition 
```bash
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/credentials-key.json
```

Aibril Conversation
```bash
export watson_username=YOUR_USER_NAME
export watson_password=YOUR_PASSWORD
export watson_workspace=YOUR_WORKSPACE
export watson_url=YOUR_URL
export watson_version=YOUR_VERSION
```

Naver Clova TTS
```bash
export naver_tts_client_id=YOUR_CLIENT_ID
export naver_tts_client_secret=YOUR_CLIENT_SECRET
```

AWS Polly TTS
- <https://github.com/yonghankim/aws-polly#3-getting-started-with-the-aws-cli>


## Getting Started
Creating virtualenv
1. `cd AI-Speaker`
2. `virtualenv env --python=python3.5`
3. `source env/bin/activate`
4. `pip install -r requirements.txt`

Run
- `python main.py`
