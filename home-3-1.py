player_name = input('Enter player name:')

player = {
    'name':player_name,
    'health':100,
    'armor':1.5,
    'damage':50
}

enemy_name = input('Enter enemy name:')
enemy = {
    'name':enemy_name,
    'health':50,
    'armor':1.2,
    'damage':30
}

def attack(unit, target):
    target['health'] -= unit['damage'] / target['armor']
    target['health'] = round(target['health'],2)


attack(player, enemy)
print(enemy)

attack(enemy, player)
print(player)

# number 4
# add armor

