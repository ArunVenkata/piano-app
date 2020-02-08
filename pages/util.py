from pydub import AudioSegment
import time


def render_audio(data):
    base = AudioSegment.silent(duration=data['TotalTime'])
    for i in data["Keys"].keys():
        audio = AudioSegment.from_wav('static/sounds/' + data['Keys'][i] + '.wav')
        base = base.overlay(audio, position=int(i))
    path = 'recordings/' + str(int(time.time())) + '.wav'
    base.export('media/' + path, format='wav')
    return path
