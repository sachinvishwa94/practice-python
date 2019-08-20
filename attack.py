'''''
import random

playerhp = 200
enmyatkl = 50
enmyatkh = 80

while playerhp > 0:

    dmg = random.randrange(enmyatkl, enmyatkh)
    playerhp = playerhp - dmg

    if playerhp <= 20:
        playerhp = 20

    print('you have been hit by HP amounting to', dmg, 'your reduced hp is', playerhp)

    if playerhp == 20:
        print("you have been knocked out and last damage was", dmg)
        break
'''''

from classes.enemy import Enemy

enemy = Enemy(200,54)

print(enemy.get_hp())
