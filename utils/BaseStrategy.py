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