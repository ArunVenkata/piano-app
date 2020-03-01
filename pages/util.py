from pydub import AudioSegment
from io import BytesIO
import time, base64


def render_audio(data):
    # base = AudioSegment.silent(duration=data['TotalTime'])
    voice = base64.b64decode(data['Audio'])
    base = AudioSegment.from_file(BytesIO(voice))
    for i in data["Keys"].keys():
        audio = AudioSegment.from_wav('static/sounds/' + data['Keys'][i] + '.wav')
        base = base.overlay(audio, position=int(i))
    path = 'recordings/' + str(int(time.time())) + '.wav'
    base.export('media/' + path, format='wav')
    return path
