from utils.BaseStrategy import BaseStrategy

"""
Strategy:
    If the tip of the pole is going left, push the pole left or vice versa
    If the position of the pole is not centered, push the pole back to the center
"""
class TipVelocityAndPositionStrategy(BaseStrategy):
    count = 0

    def calculate(self, observation):
        self.count = self.count + 1

        if self.count % 2 == 0:
            if (self.is_pole_positioned_right(observation)):
                return self.make_move_left_action()
            else:
                return self.make_move_right_action()

        if (self.is_pole_tip_velocity_left(observation)):
            return self.make_move_left_action()
        else:
            return self.make_move_right_action()