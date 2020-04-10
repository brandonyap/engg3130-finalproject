import numpy as np
import math
import random
from utils.BaseStrategy import BaseStrategy

class Agent(BaseStrategy):
    def __init__(self, actions=None, default_action_length=1000):
        self.idx = 0
        if actions:
            self.actions = actions
        else:
            self.actions = []
            for _ in range(default_action_length):
                self.actions.append(self.create_random_action())

    def reset(self):
        self.idx = 0

    def calculate(self, observation):
        if self.idx == len(self.actions):
            return self.emit_end_game_signal()
        else:
            current_action = self.actions[self.idx]
            self.idx += 1
            return current_action  

class Population:
    def __init__(self, pop_size, mutation_rate=0.01):
        self.pop_size = pop_size
        self.mutation_rate = mutation_rate
        self.agents = []
        for _ in range(pop_size):
            self.agents.append(Agent())

    def next_generation(self):        
        mating_pool, max_agent = self.create_mating_pool()
        new_agents = self.natural_selection(mating_pool)

        for agent in new_agents:
            self.mutate(agent)

        self.agents = new_agents

        return max_agent

    def calculate_max_fitness(self):
        max_fitness = -1
        max_agent = None
        for agent in self.agents:
            fitness = self.calculate_fitness(agent)
            if fitness > max_fitness:
                max_fitness = fitness
                max_agent = agent
        return max_fitness, max_agent

    def create_mating_pool(self):
        mating_pool = []

        max_fitness, max_agent = self.calculate_max_fitness()
        for agent in self.agents:
            n = math.floor(self.calculate_normalized_fitness(agent, max_fitness) * self.pop_size)
            for _ in range(n):
                mating_pool.append(agent)
        return mating_pool, max_agent

    def natural_selection(self, mating_pool):
        new_agents = []
        for _ in range(self.pop_size):
            parentA = random.choice(mating_pool)
            parentB = random.choice(mating_pool)
            child = self.crossover(parentA, parentB)
            # child = parentA.crossover(parentB)
            new_agents.append(child)
        return new_agents

    def crossover(self, parentA, parentB):
        new_actions = []

        l = len(parentA.actions)
        midpoint = math.floor(np.random.random() * l)

        for i in range(l):
            if i < midpoint:
                new_actions.append(parentA.actions[i])
            else:
                new_actions.append(parentB.actions[i])

        return Agent(actions=new_actions)

    def mutate(self, agent):
        for i in range(len(agent.actions)):
            if np.random.random() < self.mutation_rate:
                agent.actions[i] = agent.create_random_action()

    # To start objective of game is to get all 1
    def calculate_fitness(self, agent):
        total = 0
        for action in agent.actions:
            total += action
        return total

    def calculate_normalized_fitness(self, agent, max_fitness):
        return self.calculate_fitness(agent) / max_fitness