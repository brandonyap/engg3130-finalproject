import matplotlib.pyplot as plt

class Logger:
    def __init__(self):
        self.positions = []
        self.velocities = []
        self.angles = []
        self.tip_velocities = []

    def log(self, position, velocity, angle, tip_velocity):
        self.positions.append(position)
        self.velocities.append(velocity)
        self.angles.append(angle)
        self.tip_velocities.append(tip_velocity)

    def get_positions(self):
        return self.positions

    def get_velocities(self):
        return self.velocities

    def get_angles(self):
        return self.angles
        
    def get_tip_velocities(self):
        return self.tip_velocities
    
    def get_logs(self):
        return (
            self.get_positions(),
            self.get_velocities(),
            self.get_angles(),
            self.get_tip_velocities()
        )

    def plot(self, title=""):
        fig, axs = plt.subplots(4)
        if title != "":
            fig.suptitle(title)
        
        axs[0].plot(self.get_positions())
        axs[0].set(xlabel='time', ylabel='position relative to center')

        axs[1].plot(self.get_velocities())
        axs[1].set(xlabel='time', ylabel='pole base velocity')

        axs[2].plot(self.get_tip_velocities())
        axs[2].set(xlabel='time', ylabel='pole tip velocity')

        axs[3].plot(self.get_angles())
        axs[3].set(xlabel='time', ylabel='pole angle')

        plt.show()
