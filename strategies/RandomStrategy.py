from utils.BaseStrategy import BaseStrategy
import random

"""
Strategy:
    Random Strategy for going Left or Right
"""
class RandomStrategy(BaseStrategy):
    def calculate(self, observation):
        if random.random():
            return self.make_move_left_action()
        else:
            return self.make_move_right_action()