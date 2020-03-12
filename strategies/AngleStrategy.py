from utils.BaseStrategy import BaseStrategy

"""
Strategy:
    If the angle of the pole is left, push the pole left to fix the angle
    vice versa
"""
class AngleStrategy(BaseStrategy):
    def calculate(self, observation):        
        if (self.is_pole_angled_left(observation)):
            return self.make_move_left_action()
        else:
            return self.make_move_right_action()