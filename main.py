import gym
import numpy as np
import math

# Observation: 
#     Type: Box(4)
#     Num	Observation                 Min         Max
#     0	Cart Position             -4.8            4.8
#     1	Cart Velocity             -Inf            Inf
#     2	Pole Angle                 -24 deg        24 deg
#     3	Pole Velocity At Tip      -Inf            Inf
    
# Actions:
#     Type: Discrete(2)
#     Num	Action
#     0	Push cart to the left
#     1	Push cart to the right

class Logger:
    def __init__(self):
        self.positions = []
        self.velocities = []
        self.angles = []
        self.tip_velocities = []

    def log(self, position, velocity, angle, tip_velocity):
        self.positions.append(position)
        self.velocities.append(velocity)
        self.angles.append(angle)
        self.tip_velocities.append(tip_velocity)

    def get_positions(self):
        return self.positions

    def get_velocities(self):
        return self.velocities

    def get_angles(self):
        return self.angles
        
    def get_tip_velocities(self):
        return self.tip_velocities
    
    def get_logs(self):
        return (
            self.get_positions(),
            self.get_velocities(),
            self.get_angles(),
            self.get_tip_velocities()
        )


class BaseStrategy:
    def get_pole_position(self, observation):
        return observation[0]

    def get_pole_velocity(self, observation):
        return observation[1]
        
    def get_pole_angle(self, observation):
        return observation[2]

    def get_pole_tip_velocity(self, observation):
        return observation[3]

    def is_pole_positioned_right(self, observation):
        return self.get_pole_position(observation) > 0

    def is_pole_positioned_left(self, observation):
        return self.get_pole_position(observation) < 0
    
    def is_pole_moving_left(self, observation):
        return self.get_pole_velocity(observation) < 0
    
    def is_pole_moving_right(self, observation):
        return self.get_pole_velocity(observation) > 0

    def is_pole_angled_left(self, observation):
        return self.get_pole_angle(observation) < 0
    
    def is_pole_angled_right(self, observation):
        return self.get_pole_angle(observation) > 0

    def make_move_right_action(self):
        return 1

    def make_move_left_action(self):
        return 0

class PositionStrategy(BaseStrategy):
    def calculate(self, observation):
        if (self.is_pole_angled_left(observation)):
            return self.make_move_left_action()
        else:
            return self.make_move_right_action()

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

    def play(self):
        observation, reward, done, info = self.env.step(0)
        for _ in range(self.steps):
            self.env.render()
            action = self.strategy.calculate(observation)
            observation, reward, done, info = self.env.step(action)
            self.log(observation)

    def close(self):
        self.env.close()

def play_game(strategy, steps=1000):
    game = Game(steps, strategy())
    game.play()
    game.close()
    game.print_logs()

if __name__ == '__main__':
    play_game(PositionStrategy, 10)

# adding a comment