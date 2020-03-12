from utils.Logger import Logger
import gym

class Game:
    def __init__(self, steps, strategy):
        self.steps = steps
        self.strategy = strategy
        self.logger = Logger()

        self.env = gym.make('CartPole-v0')
        self.env.reset()

    def log(self, observation):
        self.logger.log(
            self.strategy.get_pole_position(observation),
            self.strategy.get_pole_velocity(observation),
            self.strategy.get_pole_angle(observation),
            self.strategy.get_pole_tip_velocity(observation)
        )

    def print_logs(self):
        print(self.logger.get_positions())
        print(self.logger.get_velocities())
        print(self.logger.get_angles())
        print(self.logger.get_tip_velocities())

    def plot(self, title=""):
        self.logger.plot(title)

    def play(self):
        observation, reward, done, info = self.env.step(0)
        for _ in range(self.steps):
            self.env.render()
            action = self.strategy.calculate(observation)
            observation, reward, done, info = self.env.step(action)
            self.log(observation)

    def close(self):
        self.env.close()