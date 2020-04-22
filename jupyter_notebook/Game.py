from Logger import Logger, ScoreLogger
import gym

class Game:
    def __init__(self, episodes, strategy, render=False):
        self.episodes = episodes
        self.strategy = strategy
        self.logger = Logger()
        self.scorelogger = ScoreLogger()
        self.render = render
        self.highscore = -1
        self.totalscore = 0

        self.env = gym.make('CartPole-v1')

    def log_score(self, score):
        self.totalscore += score
        self.scorelogger.log(score)

    def log_observation(self, observation, logger):
        logger.log(
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
         print(self.scorelogger.get_scores())

    def plot(self, title=""):
        print("High Score: " + str(self.highscore) + ", Average Score: " + str(self.totalscore/self.episodes))
        self.scorelogger.plot(title)
        self.logger.plot(title)

    def play(self):
        for episode in range(self.episodes):
            self.env.reset()
            observation, reward, done, info = self.env.step(0)

            step = 0
            logger = Logger()

            while True:
                step += 1
                if self.render:
                    self.env.render()
                action = self.strategy.calculate(observation)
                observation, reward, done, info = self.env.step(action)

                self.log_observation(observation, logger)

                if done:
                    self.log_score(step)
                    # print("Run: " + str(episode+1) + ", score: " + str(step))
                    if step > self.highscore:
                        self.highscore = step
                        self.logger = logger
                    break

    def close(self):
        self.env.close()


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

class BaseStrategy:
    MAX_POSITION_RIGHT = 4.8
    MAX_POSITION_LEFT = -4.8

    def get_pole_position(self, observation):
        return observation[0]

    def is_pole_positioned_right(self, observation):
        return self.get_pole_position(observation) > 0

    def is_pole_positioned_left(self, observation):
        return self.get_pole_position(observation) < 0

    def get_pole_velocity(self, observation):
        return observation[1]

    def is_pole_moving_left(self, observation):
        return self.get_pole_velocity(observation) < 0
    
    def is_pole_moving_right(self, observation):
        return self.get_pole_velocity(observation) > 0
        
    def get_pole_angle(self, observation):
        return observation[2]

    def is_pole_angled_left(self, observation):
        return self.get_pole_angle(observation) < 0
    
    def is_pole_angled_right(self, observation):
        return self.get_pole_angle(observation) > 0

    def get_pole_tip_velocity(self, observation):
        return observation[3]
    
    def is_pole_tip_velocity_right(self, observation):
        return self.get_pole_tip_velocity(observation) > 0

    def is_pole_tip_velocity_left(self, observation):
        return self.get_pole_tip_velocity(observation) < 0

    def make_move_right_action(self):
        return 1

    def make_move_left_action(self):
        return 0

