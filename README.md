# AppPythonRobotic
Premier Projet robotique que j'ai fait avec python

Le programme va démarrer le moteur avec la fan et le Ultasonic sensor va commencer à envoyer du son qui va nous donner la distance, si la distance est de moins de 15 cm, le moteur va arrêter et Le LED 8X8 va afficher un point d'interrogation. Également, le LCD va afficher constamment la distance en cm. Si la distance est a moins de 10 cm, la LED8x8 va afficher une croix avec la lumière et l'écran LCD va remplacer le message de la distance en cm par un message de danger. 

On va utiliser des librairies : 
- import board 
- import digitalio 
- import adafruit_character_lcd.character_lcd as CharLCD 
- from time import sleep 
- Import pigpio 
-  from adafruit_ads1x15.ads1115 import P0 
- from adafruit_ads1x15.ads1115 import ADS1115 
- from adafruit_ads1x15.analog_in import AnalogIn 
- import adafruit_bus_device.i2c_device as i2c_device 
- from adafruit_ht16k33 import matrix 

 

Pour les installer faire ces commandes;  

pip3 install adafruit-circuitpython-ht16k33 

sudo pip3 install adafruit-circuitpython-ads1x15 --break-system-packages 

sudo pip3 install adafruit-circuitpython-charlcd --break-system-packages 
