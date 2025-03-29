import pygame
pygame.init()
pygame.mixer.music.load('UmSonho.mp3')
pygame.mixer.music.play()
input()                                                 # É necessário colocar input() na nova versão
pygame.event.wait()