# 🤖 RobotGuard: Système de Sécurité Robotique avec Python

## Description du projet :
RobotGuard est un projet robotique simple développé en Python, utilisant une combinaison de capteurs et d'affichages pour créer un système de sécurité autonome. Ce programme contrôle un moteur, un ventilateur, un capteur ultrason, une LED 8x8, et un écran LCD pour détecter les obstacles et afficher des informations critiques en temps réel.

## Fonctionnement du système :

Moteur et Ventilateur : Au démarrage, le moteur et le ventilateur sont activés.

Capteur Ultrason : Un capteur ultrason émet des ondes sonores et mesure la distance entre le robot et un obstacle. Si la distance est inférieure à 15 cm, le moteur s'arrête immédiatement.

Affichage LED 8x8 : Si l'obstacle est détecté à moins de 15 cm, le module LED 8x8 affiche un point d'interrogation (?). Si la distance est inférieure à 10 cm, la LED affiche une croix, signalant un danger imminent.

Affichage LCD : L'écran LCD affiche constamment la distance en centimètres. Si la distance devient inférieure à 10 cm, le message sur l'écran LCD est remplacé par un avertissement de "DANGER".

## Librairies utilisées :

board

* digitalio

* adafruit_character_lcd.character_lcd pour l'écran LCD

* time pour les délais

* pigpio pour le contrôle des GPIO

* adafruit_ads1x15.ads1115 et adafruit_ads1x15.analog_in pour la lecture des capteurs analogiques

* adafruit_bus_device.i2c_device pour la gestion des périphériques I2C

* adafruit_ht16k33 pour le contrôle du module LED 8x8

* Installation des dépendances :

### Pour installer les bibliothèques nécessaires, exécutez les commandes suivantes :
```bash
pip3 install adafruit-circuitpython-ht16k33
sudo pip3 install adafruit-circuitpython-ads1x15 --break-system-packages
sudo pip3 install adafruit-circuitpython-charlcd --break-system-packages
```
