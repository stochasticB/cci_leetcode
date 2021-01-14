import random


class FairRoulette():
    def __init__(self):
        self.pockets = []

        # 36 pockets: bet 1-36
        for i in range(1, 37):
            self.pockets.append(i)
        self.ball = None

        # if you bet $1, you get $36 back ($1 you bet, $35 win)
        self.pocketOdds = len(self.pockets) - 1

    def spin(self):
        self.ball = random.choice(self.pockets)

    def betPocket(self, pocket, amt):
        if str(pocket) == str(self.ball):
            return amt*self.pocketOdds
        else: return -amt

    def __str__(self):
        return 'Fair Roulette'


def playRoulette(game, numSpins, pocket, bet, toPrint):
    totPocket = 0
    for i in range(numSpins):
        game.spin()
        totPocket += game.betPocket(pocket, bet)
    if toPrint:
        print(numSpins, 'spins of', game)
        print('Expected return betting', pocket, '=', str(100*totPocket/numSpins) + '%\n')
    return totPocket/numSpins


random.seed(0)
game = FairRoulette()
for numSpins in (100, 1000000):
    for i in range(3):
        playRoulette(game, numSpins, 2, 1, True)
