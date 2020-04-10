from strategies.GeneticAlgorithm import Population
pop_size = 100
action_length = 50
mutation_rate = 0.001
num_generations = 500



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

    pop = Population(pop_size, action_length, mutation_rate)
    for _ in range(num_generations):
        max_agent = pop.next_generation()
        print(max_agent.calculate_fitness())
