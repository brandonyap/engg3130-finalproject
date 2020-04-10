import numpy as np
import math
import random
import gym
from utils.BaseStrategy import BaseStrategy

class Agent(BaseStrategy):
    def __init__(self, default_action_length, actions=None):
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
            print(str(current_action) + " " + str(self.idx))
            return current_action

    def calculate_fitness(self, env):
        total = 0

        for action in self.actions:
            observation, reward, done, info = env.step(action)
            if done:
                break
            else:
                total += 1

        return total

class Population:
    def __init__(self, pop_size, mutation_rate=0.01, default_action_length=1000):
        self.pop_size = pop_size
        self.mutation_rate = mutation_rate
        self.agents = []
        self.env = gym.make('CartPole-v1')
        self.default_action_length = default_action_length

        for _ in range(pop_size):
            self.agents.append(Agent(default_action_length=self.default_action_length))

    def next_generation(self):        
        mating_pool, max_agent, max_fitness = self.create_mating_pool()
        new_agents = self.natural_selection(mating_pool)

        for agent in new_agents:
            self.mutate(agent)

        self.agents = new_agents

        return max_agent, max_fitness

    def calculate_max_fitness(self):
        max_fitness = -1
        max_agent = None
        for agent in self.agents:
            self.env.reset()
            fitness = agent.calculate_fitness(self.env)
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
        return mating_pool, max_agent, max_fitness

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

        return Agent(actions=new_actions, default_action_length=self.default_action_length)

    def mutate(self, agent):
        for i in range(len(agent.actions)):
            if np.random.random() < self.mutation_rate:
                agent.actions[i] = agent.create_random_action()

    def calculate_normalized_fitness(self, agent, max_fitness):
        self.env.reset()
        return agent.calculate_fitness(self.env) / max_fitness