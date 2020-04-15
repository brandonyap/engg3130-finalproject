from utils.BaseStrategy import BaseStrategy
from utils.Game import Game
from strategies.PositionStrategy import PositionStrategy
from strategies.AngleStrategy import AngleStrategy
from strategies.TipVelocityStrategy import TipVelocityStrategy
from strategies.TipVelocityAndPositionStrategy import TipVelocityAndPositionStrategy
from strategies.RandomStrategy import RandomStrategy

episodes = 100
render=False

def play_game(strategy, title="", episodes=100):
    print(title)
    game = Game(episodes, strategy(), render)
    game.play()
    game.close()
    game.plot(title)

if __name__ == '__main__':
    play_game(PositionStrategy, "Position Strategy", episodes)
    play_game(AngleStrategy, "Angle Strategy", episodes)
    play_game(TipVelocityStrategy, "Tip Velocity Strategy", episodes)
    play_game(TipVelocityAndPositionStrategy, "Tip Velocity and Position Strategy", episodes)
    play_game(RandomStrategy, "Random Strategy", episodes)
