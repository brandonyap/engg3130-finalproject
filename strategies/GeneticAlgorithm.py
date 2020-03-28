import numpy as np
import math
import random

class Agent:
    def __init__(self, action_length, actions=None):
        self.observations = []
        self.action_length = action_length
        if actions == None:
            self.actions = []        
            for _ in range(action_length):
                self.actions.append(Agent.create_random_action())
        else:
            self.actions = actions

    @staticmethod
    def create_random_action():
        r = np.random.random()
        if (r > 0.5):
            return 1
        else:
            return 0

    def play(self):
        self.observations = []
        # to start I am just going to make the goal of the game to make all of your actions 1
        for action in self.actions:
            self.observations.append(action)

    def calculate_fitness(self):
        total = 0
        for obs in self.observations:
            total += obs
        return total

    def calculate_normalized_fitness(self, max_fitness):
        return self.calculate_fitness() / max_fitness

    def crossover(self, other):
        new_actions = []
        midpoint = math.floor(np.random.random() * self.action_length)
        for i in range(self.action_length):
            if i < midpoint:
                new_actions.append(self.actions[i])
            else:
                new_actions.append(other.actions[i])
        return Agent(self.action_length, new_actions)

    def mutate(self, mutation_rate):
        for i in range(self.action_length):
            r = np.random.random()
            if r < mutation_rate:
                self.actions[i] = Agent.create_random_action()        

class Population:
    def __init__(self, popsize, action_length, mutation_rate=0.01): #, agents=None
        self.popsize = popsize
        self.mutation_rate = mutation_rate
        self.agents = []
        for _ in range(popsize):
            self.agents.append(Agent(action_length))

    def next_generation(self):
        for agent in self.agents:
            agent.play()
        
        mating_pool, max_agent = self.create_mating_pool()
        new_agents = self.natural_selection(mating_pool)

        for agent in new_agents:
            agent.mutate(self.mutation_rate)

        self.agents = new_agents

        return max_agent

    def calculate_max_fitness(self):
        max_fitness = -1
        max_agent = None
        for agent in self.agents:
            fitness = agent.calculate_fitness()
            if fitness > max_fitness:
                max_fitness = fitness
                max_agent = agent
        return max_fitness, max_agent

    def create_mating_pool(self):
        mating_pool = []

        max_fitness, max_agent = self.calculate_max_fitness()
        for agent in self.agents:
            normalized_fitness = agent.calculate_normalized_fitness(max_fitness)
            n = math.floor(normalized_fitness * self.popsize)
            for _ in range(n):
                mating_pool.append(agent)
        return mating_pool, max_agent

    def natural_selection(self, mating_pool):
        new_agents = []
        for _ in range(self.popsize):
            parentA = random.choice(mating_pool)
            parentB = random.choice(mating_pool)
            child = parentA.crossover(parentB)
            new_agents.append(child)
        return new_agents