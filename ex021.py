#Faça um programa que abra e reproduza o áudio de um arquivo MP3.

import vlc

media = vlc.MediaPlayer('As_It_Was.mp4')
media.play()