from utils.BaseStrategy import BaseStrategy
from utils.Game import Game
from strategies.PositionStrategy import PositionStrategy
from strategies.AngleStrategy import AngleStrategy
from strategies.TipVelocityStrategy import TipVelocityStrategy
from strategies.TipVelocityAndPositionStrategy import TipVelocityAndPositionStrategy
from strategies.RandomStrategy import RandomStrategy
from strategies.GeneticAlgorithm import Population

def play_game(strategy, title="", episodes=100, render=False, plot=True):
    print(title)
    game = None
    game = Game(episodes, strategy, render)
    game.play()
    game.close()
    if plot:
        game.plot(title)

def train_genetic_algorithm(pop_size=100, mutation_rate=0.001):
    pop = Population(pop_size, mutation_rate)
    max_agent = None
    for _ in range(500):
        max_agent = pop.next_generation()
        print(pop.calculate_fitness(max_agent))
    return max_agent

if __name__ == '__main__':
    # play_game(PositionStrategy(), "Position Strategy", plot=False)
    # play_game(AngleStrategy(), "Angle Strategy", plot=False)
    # play_game(TipVelocityStrategy(), "Tip Velocity Strategy", plot=False)
    # play_game(TipVelocityAndPositionStrategy(), "Tip Velocity and Position Strategy", plot=False)
    # play_game(RandomStrategy(), "Random Strategy", plot=False)

    max_agent = train_genetic_algorithm()
    print(max_agent)

    play_game(max_agent, "Genetic Algorithm", render=True)
