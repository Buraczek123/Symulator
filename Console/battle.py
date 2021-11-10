from exceptions import *
from os import system

class Battle:
    def battle(player, defender):
        turn = 1
        try:
            system("cls")
            print(f"You've encountered {defender.getName()}")
            while player.isAlive() and defender.isAlive():
                print(f"Turn {turn}\n")
                player.chooseMove()(defender)
                if defender.isAlive():
                    defender.attack(player)
                else:
                    player.giveXp(defender.getXp())
                    raise BattleEnd(player)
                if not player.isAlive():
                    raise BattleEnd(defender)
                turn += 1
        except BattleEnd as e:
            print(f"{e.winner.getName()} won battle.\n")
        input("...")
