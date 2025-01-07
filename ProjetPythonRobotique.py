import pigpio
import time
from time import sleep
import board
import digitalio
import adafruit_character_lcd.character_lcd as CharLCD
from time import sleep
from gpiozero import Servo
# Connexions
# VCC   5V
# Trig  GPIO 18
# Echo  GPIO 23
# Gnd   GND
cols = 8
rows = 2
TRIG = 18
ECHO = 23
servo = 17 # Le numéro GPIO de la broche ou est connecté le servomoteur
FREQ = 50 # Fréquence en Hz de la période

## board.D1 = GPIO 1, board.D2 = GPIO 2, etc.
## Mettez ici les valeurs qui correspondent à vos connexions
RS = digitalio.DigitalInOut(board.D26)
E = digitalio.DigitalInOut(board.D19)
DB7 = digitalio.DigitalInOut(board.D5)
DB6 = digitalio.DigitalInOut(board.D6)
DB5 = digitalio.DigitalInOut(board.D8)
DB4 = digitalio.DigitalInOut(board.D7)


pi = pigpio.pi()

pi.set_mode(TRIG, pigpio.OUTPUT)
pi.set_mode(ECHO, pigpio.INPUT)

pi.set_mode(servo,pigpio.OUTPUT)
pi.set_PWM_frequency(servo,FREQ)
pi.set_PWM_range(servo,100) # Valeurs possibles dutycycle de 0-100
plus90 = 12.5
moins90 = 2.5
moitier = 7.5
            # Envoyer un son

try:
    lcd = CharLCD.Character_LCD(RS,E,DB4,DB5,DB6,DB7,cols,rows)
    lcd.message = "WELCOME"
    sleep(1)
    
    while True:
            
            lcd.clear()
            lcd.message = "DISTANCE"
            pi.set_PWM_dutycycle(servo,plus90)
            sleep(0.5)#0.5
            pi.set_PWM_dutycycle(servo,moitier)
            sleep(0.5)#0.5
            pi.set_PWM_dutycycle(servo,moins90)
            
            pi.write(TRIG, 1)
            time.sleep(0.00001)
            pi.write(TRIG, 0)

            # Attendre l'echo
            debut = time.time()
            while pi.read(ECHO) == 0:
                # Break si on attend le debut de l'echo plus que 1 seconde
                if time.time() - debut > 1: 
                    break

            # Echo arrive
            echo = time.time()
            while pi.read(ECHO) == 1:
                # Break si on attend la fin de l'écho plus que 1 seconde
                if time.time() - echo > 1: 
                    break

            # Duree de l'echo
            duree = time.time() - echo

            # Calculer la distance
            distanceInt = int((duree * 34300) / 2)
            if distanceInt is not None:
                print(f"Distance mesurée : {distanceInt} cm")
                sleep(0.5)
            else:
                print("erreur")
            


            nb = str(distanceInt)
            lcd.clear()
            lcd.cursor_position(0,1)
            lcd.message = nb +" cm "
            sleep(1)
            lcd.clear()
            
        

except KeyboardInterrupt:
    print("Le programme s'est terminé")
    pi.stop()