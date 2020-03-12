from utils.BaseStrategy import BaseStrategy
from utils.Game import Game
from strategies.PositionStrategy import PositionStrategy

def play_game(strategy, steps=1000):
    game = Game(steps, strategy())
    game.play()
    game.close()
    game.plot()

if __name__ == '__main__':
    play_game(PositionStrategy, 100)
