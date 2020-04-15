from utils.BaseStrategy import BaseStrategy

"""
Strategy:
    If the position of the pole is left of the center, push the pole right or vice versa
"""
class PositionStrategy(BaseStrategy):
    def calculate(self, observation):        
        if (self.is_pole_positioned_right(observation)):
            return self.make_move_left_action()
        else:
            return self.make_move_right_action()
