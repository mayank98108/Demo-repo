from django.shortcuts import render
from django.http import StreamingHttpResponse
import threading
# Create your views here.
import pyaudio
import wave
import cv2

def test():

    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 10
    WAVE_OUTPUT_FILENAME = "file.wav"

    audio = pyaudio.PyAudio()

    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    print ("recording...")
    #frames = []

    #for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    frames = stream.read(CHUNK)
    #frames.append(data)
    print ("finished recording")


    # stop Recording
    #stream.stop_stream()
    #stream.close()
    #audio.terminate()

    #waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    #waveFile.setnchannels(CHANNELS)
    #waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    #waveFile.setframerate(RATE)
    #waveFile.writeframes(b''.join(frames))
    #waveFile.close()

    #return WAVE_OUTPUT_FILENAME



    yield(b'--frame\r\n'
                b'Content-Type: audio/mp3\r\n\r\n' + frames + b'\r\n\r\n')

#@gzip.gzip_page

def home(request):
	return StreamingHttpResponse(test(), content_type="audio/x-wav", status=206)
