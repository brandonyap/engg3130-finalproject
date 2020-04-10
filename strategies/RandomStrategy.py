from utils.BaseStrategy import BaseStrategy
import random

"""
Strategy:
    Random Strategy for going Left or Right
"""
class RandomStrategy(BaseStrategy):
    def calculate(self, observation):
        return self.create_random_action()