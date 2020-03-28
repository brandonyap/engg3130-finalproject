# from utils.BaseStrategy import BaseStrategy
# from utils.Game import Game
# from strategies.PositionStrategy import PositionStrategy
# from strategies.AngleStrategy import AngleStrategy
# from strategies.TipVelocityStrategy import TipVelocityStrategy
# from strategies.TipVelocityAndPositionStrategy import TipVelocityAndPositionStrategy

# def play_game(strategy, title="", steps=1000):
#     game = Game(steps, strategy())
#     game.play()
#     game.close()
#     game.plot(title)

# if __name__ == '__main__':
#     play_game(PositionStrategy, "Position Strategy", 100)
#     play_game(AngleStrategy, "Angle Strategy", 100)
#     play_game(TipVelocityStrategy, "Tip Velocity Strategy", 100)
#     play_game(TipVelocityAndPositionStrategy, "Tip Velocity and Position Strategy", 300)

from strategies.GeneticAlgorithm import Population
pop_size = 100
action_length = 50
mutation_rate = 0.001
num_generations = 500

pop = Population(pop_size, action_length, mutation_rate)
for _ in range(num_generations):
    max_agent = pop.next_generation()
    print(max_agent.calculate_fitness())
# for agent in pop.pop:
#     print(agent)
#     for action in agent.actions:
#         print(action)