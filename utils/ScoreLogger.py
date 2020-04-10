import matplotlib.pyplot as plt

class ScoreLogger:
    def __init__(self):
        self.scores = []

    def log(self, scores):
        self.scores.append(scores)

    def get_scores(self):
        return self.scores

    def plot(self, title=""):
        fig, ax = plt.subplots()
        ax.plot(self.scores)

        ax.set(xlabel='Episode', ylabel='Score',
            title=title)

        plt.show()