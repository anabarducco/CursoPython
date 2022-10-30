#Faça um programa que abra e reproduza o áudio de um arquivo MP3.

'''import vlc

media = vlc.MediaPlayer('As_It_Was.mp4')
media.play()'''

import pygame

pygame.init()
pygame.display.set_mode((200,100))
pygame.mixer.music.load('As_It_Was.ogg')
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(0)
pygame.event.wait()