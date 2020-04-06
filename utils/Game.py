from utils.ScoreLogger import ScoreLogger
import gym

class Game:
    def __init__(self, episodes, strategy, render=False):
        self.episodes = episodes
        self.strategy = strategy
        self.logger = ScoreLogger()
        self.render = render

        self.env = gym.make('CartPole-v1')

    def log(self, score):
        self.logger.log(score)

    def plot(self, title=""):
        self.logger.plot(title)

    def play(self):
        episode = 0
        while episode < self.episodes:
            episode += 1

            self.env.reset()
            observation, reward, done, info = self.env.step(0)

            step = 0

            while True:
                step += 1
                if self.render:
                    self.env.render()
                action = self.strategy.calculate(observation)
                observation, reward, done, info = self.env.step(action)
                if done:
                    self.log(step)
                    print("Run: " + str(episode) + ", score: " + str(step))
                    break

    def close(self):
        self.env.close()