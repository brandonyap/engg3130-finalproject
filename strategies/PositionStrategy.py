from utils.BaseStrategy import BaseStrategy

class PositionStrategy(BaseStrategy):
    def calculate(self, observation):
        if (self.is_pole_angled_left(observation)):
            return self.make_move_left_action()
        else:
            return self.make_move_right_action()