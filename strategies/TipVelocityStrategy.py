from utils.BaseStrategy import BaseStrategy

"""
Strategy:
    If the tip of the pole is going left, push the pole left or vice versa
"""
class TipVelocityStrategy(BaseStrategy):
    def calculate(self, observation):        
        if (self.is_pole_tip_velocity_left(observation)):
            return self.make_move_left_action()
        else:
            return self.make_move_right_action()
