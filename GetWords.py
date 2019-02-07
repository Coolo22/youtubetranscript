from __future__ import unicode_literals
import speech_recognition as sr
from os import path
from pydub import AudioSegment
from pytube import YouTube
import os, sys, time, ffmpeg, urllib.error, re, pipes, random, youtube_dl
import lxml, urllib, urllib.request
from lxml import etree
from urllib import request



def video_to_audio(fileName):
	try:
		file, file_extension = os.path.splitext(fileName)
		file = pipes.quote(file)
		video_to_wav = 'ffmpeg -i ' + file + file_extension + ' ' + file + '.wav'
		final_audio = 'lame '+ file + '.wav' + ' ' + file + '.mp3'
		os.system(video_to_wav)
		os.system(final_audio)
		#file=pipes.quote(file)
		#os.remove(file + '.wav')
		print("sucessfully converted ", fileName, " into audio!")
	except OSError as err:
		print(err.reason)
		exit(1)


filenamerandom = str(random.randint(1, 10000))
yt = input("What video URL?")
print("Fetching Video.")

youtube = etree.HTML(urllib.request.urlopen(yt).read())
video_title = youtube.xpath("//span[@id='eow-title']/@title")
print(''.join(video_title))
title = ''.join(video_title)


paths = os.path.dirname(sys.argv[0])
path = os.path.abspath(paths) + "\\"



import pafy
video = pafy.new(yt)
bestaudio = video.getbestaudio()
bestaudio.bitrate #get bit rate
bestaudio.extension #extension of audio fileurl
...
bestaudio.url #get url
...

bestaudio.download(filenamerandom + ".mp4")



print("Converting video to audio")
video_to_audio(filenamerandom + ".mp4")
print("Done")




AUDIO_FILE = filenamerandom + ".wav"

# use the audio file as the audio source                                        
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file                  

        print("Transcription: " + r.recognize_google(audio))

