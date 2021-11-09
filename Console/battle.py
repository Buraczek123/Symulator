class Battle:
    def battle(player, defender):
        print()
        while player.isAlive() and defender.isAlive():
            player.chooseMove()(defender)
            if defender.isAlive():
                defender.attack(player)
            print()
        input("...")
