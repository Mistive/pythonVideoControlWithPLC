#-*- coding:utf-8 -*-
#Youtube download module is pytube3, pytube.
#pytube3 is available to python 3.6/7/8
#if you download both, happen to abort
from pytube import YouTube

yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')

print(yt.streams.filter())