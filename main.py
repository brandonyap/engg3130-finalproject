from utils.BaseStrategy import BaseStrategy
from utils.Game import Game
from strategies.PositionStrategy import PositionStrategy
from strategies.AngleStrategy import AngleStrategy

def play_game(strategy, title="", steps=1000):
    game = Game(steps, strategy())
    game.play()
    game.close()
    game.plot(title)

if __name__ == '__main__':
    play_game(PositionStrategy, "Position Strategy", 100)
    play_game(AngleStrategy, "Angle Strategy", 100)
