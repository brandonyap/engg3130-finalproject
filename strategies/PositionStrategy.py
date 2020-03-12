from utils.BaseStrategy import BaseStrategy

class PositionStrategy(BaseStrategy):
    def calculate(self, observation):
        pos = self.get_pole_position(observation)
        if (pos > self.MAX_POSITION_RIGHT):
            return self.make_move_left_action()
        elif (pos < self.MAX_POSITION_LEFT):
            return self.make_move_right_action()
        
        if (self.is_pole_angled_left(observation)):
            return self.make_move_left_action()
        else:
            return self.make_move_right_action()