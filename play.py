#import pygame
#pygame.mixer.music.load('theme.mp3')
#pygame.mixer.music.play(-1)
 
import pyaudio
import wave

wf1 = wave.open("theme.wav", 'rb')
wf1 = wave.open("rebuild.wav", 'rb')

def callback(in_data, frame_count, time_info, status):
    data1 = wf.readframes(frame_count)
    data2 = wf1.readframes(frame_count)
    decodeddata1 = numpy.fromstring(data1, numpy.int16)
    decodeddata2 = numpy.fromstring(data2, numpy.int16)
    newdata = (decodeddata1 * 0.5 + decodeddata2* 0.5).astype(numpy.int16)
    return (result.tostring(), pyaudio.paContinue)