from utils.BaseStrategy import BaseStrategy
from utils.Game import Game
from strategies.PositionStrategy import PositionStrategy
from strategies.AngleStrategy import AngleStrategy
from strategies.TipVelocityStrategy import TipVelocityStrategy
from strategies.TipVelocityAndPositionStrategy import TipVelocityAndPositionStrategy
from strategies.RandomStrategy import RandomStrategy
from strategies.GeneticAlgorithm import Population, Agent

def play_game(strategy, title="", episodes=100, render=False, plot=True):
    print(title)
    game = None
    game = Game(episodes, strategy, render)
    game.play()
    game.close()
    if plot:
        game.plot(title)

def train_genetic_algorithm(pop_size=100, mutation_rate=0.001, default_action_length=1000, training_episodes=500):
    pop = Population(pop_size, mutation_rate, default_action_length)
    m_max_agent = None
    m_max_fitness = 0

    for episode in range(training_episodes):
        max_agent, max_fitness = pop.next_generation()
        if max_fitness > m_max_fitness:
            m_max_fitness = max_fitness
            m_max_agent = max_agent
        print(str(m_max_fitness) + " " + str(episode) + "/" + str(training_episodes))

    return m_max_agent, m_max_fitness

if __name__ == '__main__':
    # play_game(PositionStrategy(), "Position Strategy", render=True, episodes=1)
    # play_game(AngleStrategy(), "Angle Strategy", plot=False)
    # play_game(TipVelocityStrategy(), "Tip Velocity Strategy", plot=False)
    # play_game(TipVelocityAndPositionStrategy(), "Tip Velocity and Position Strategy", plot=False)
    # play_game(RandomStrategy(), "Random Strategy", plot=False)

    max_agent, max_fitness = train_genetic_algorithm(pop_size=1000, mutation_rate=0.01, default_action_length=1000, training_episodes=1000)
    print(max_agent)
    print(max_fitness)

    # play_game(max_agent, "Genetic Algorithm", render=True)

    # play_game(Agent(), "Genetic Algorithm", render=True, episodes=1)

