# Reference: https://medium.com/@siddharthkale/solving-cartpole-v1-4be909b7c2c6

import gym
import random
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import rmsprop, Adam
import numpy as np
import matplotlib.pyplot as plt
from collections import deque
from statistics import mean
import h5py

from utils.BaseStrategy import BaseStrategy
from utils.ScoreLogger import ScoreLogger
from utils.Logger import Logger

LEARNING_RATE = 1e-3
MAX_MEMORY = 1000000
BATCH_SIZE = 20
GAMMA = 0.95
EXPLORATION_DECAY = 0.995
EXPLORATION_MIN = 0.01


class Network:

    def __init__(self, observation_space, action_space):

        self.action_space = action_space
        self.memory = deque(maxlen=MAX_MEMORY)
        self.exploration_rate = 1.0

        self.model = Sequential()
        self.model.add(Dense(32, input_shape=(observation_space,), activation='relu'))
        self.model.add(Dense(32, activation='relu'))
        self.model.add(Dense(self.action_space, activation='linear'))
        self.model.compile(loss='mse', optimizer=Adam(lr=LEARNING_RATE))

    def add_to_memory(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def take_action(self, state):
        if np.random.rand() < self.exploration_rate:
            return random.randrange(0, self.action_space)
        q_values = self.model.predict(state)
        return np.argmax(q_values[0])

    def experience_replay(self):
        if len(self.memory) < BATCH_SIZE:
            return
        else:
            minibatch = random.sample(self.memory, BATCH_SIZE)
            for state, action, reward, state_next, done in minibatch:
                Q = reward
                if not done:
                    Q = (reward + GAMMA * np.amax(self.model.predict(state_next)[0]))
                Q_values = self.model.predict(state)
                Q_values[0][action] = Q
                self.model.fit(state, Q_values, verbose=0)
            self.exploration_rate *= EXPLORATION_DECAY
            self.exploration_rate = max(EXPLORATION_MIN, self.exploration_rate)

    def get_model(self):
        return self.model


class DQNGameSolver(BaseStrategy):

    def __init__(self, max_episodes, render=False):
        self.max_episodes = max_episodes
        self.logger = Logger()
        self.scorelogger = ScoreLogger()
        self.render = render
        self.highscore = -1
        self.totalscore = 0

        self.score_table = deque(maxlen=400)
        self.average_of_last_runs = None
        self.model = None
        env = gym.make('CartPole-v1')
        observation_space = env.observation_space.shape[0]
        action_space = env.action_space.n
        self.solver = Network(observation_space, action_space)

    def log_score(self, score):
        self.totalscore += score
        self.scorelogger.log(score)

    def log_observation(self, observation, logger):
        logger.log(
             self.get_pole_position(observation),
             self.get_pole_velocity(observation),
             self.get_pole_angle(observation),
             self.get_pole_tip_velocity(observation)
         )

    def plot(self, title=""):
        print("High Score: " + str(self.highscore) + ", Average Score: " + str(self.totalscore/self.max_episodes))
        self.scorelogger.plot(title)
        self.logger.plot(title)
        
    def print_logs(self):
         print(self.logger.get_positions())
         print(self.logger.get_velocities())
         print(self.logger.get_angles())
         print(self.logger.get_tip_velocities())
         print(self.scorelogger.get_scores())

    def play(self):
        env = gym.make('CartPole-v1')
        observation_space = env.observation_space.shape[0]
        action_space = env.action_space.n

        print("---------------------------------")
        print("Solver starts")
        print("---------------------------------")

        self.model = self.solver.get_model()
        episode = 0
        while episode < self.max_episodes:

            episode += 1
            state = env.reset()
            state = np.reshape(state, [1, observation_space])
            step = 0
            logger = Logger()

            while True:

                step += 1
                if self.render:
                    env.render()
                
                action = self.solver.take_action(state)
                state_next, reward, done, info = env.step(action)

                self.log_observation(state_next, logger)

                if not done:
                    reward = reward
                else:
                    reward = -reward
                state_next = np.reshape(state_next, [1, observation_space])
                self.solver.add_to_memory(state, action, reward, state_next, done)
                state = state_next

                if done:
                    self.log_score(step)
                    print("Run: " + str(episode) + ", exploration: " + str(self.solver.exploration_rate) + ", score: " + str(step))
                    if step > self.highscore:
                        self.highscore = step
                        self.logger = logger

                    env.close()
                    break
                self.solver.experience_replay()

    def return_trained_model(self):
        return self.model

    def save_model(self):
        self.model.save('cartpole_model.h5')