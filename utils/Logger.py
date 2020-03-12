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
