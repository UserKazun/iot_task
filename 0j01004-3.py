import RPi.GPIO as GPIO
import time
import pygame.mixer

def GPIO_setup(SW1=7, LED1=21):
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(SW1, GPIO.IN)
   GPIO.setup(LED1, GPIO.OUT)
   

