#faça um programa que abra e reproduza um audio mp3 ESSE FOI DIFÍCIL
import pygame

pygame.init()
pygame.mixer.music.load('desafio21.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input()