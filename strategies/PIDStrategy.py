import control
from utils.BaseStrategy import BaseStrategy
import math

"""
m: mass of pendulum 
M: mass of cart
b: coefficient of friction of the cart (zero in this case)
I: inertia of the pendulum (might be 0?)
l = length of the pendulum 
q = (M+m) * (I+m*(l^2))-((m*l)^2)
closed loop transfer_function = Theta(s)/Force(s) = (-m*l*s)/q)  / ( (s^3) + ((b*(m(l^2) + I)/q)*(s^2) + (((M + m)*g*m*l)/q)*s +  b*m*g*l/q

No significance to values for this model
kd = 1
kp = 1
ki = 1
pid_controller = kd*s + kp + (ki/s)
open_loop_transfer_function = ((-self.m*self.l)/q) / ((s^2) + (((self.M + self.m)*self.g*self.m*self.l)/q))

"""

class PIDStrategy(BaseStrategy):

        def __init__(self):
                self.g = 9.8
                self.m = 0.1
                self.M = 1.0
                self.l = 1.0 # or 0.5?
                self.I = 0

        def pid_controller_pendulum (self, observation):

                error = (180/math.pi) * self.get_pole_angle(observation)
                #amount of deviation from vertical 

                q = (self.M+self.m) * (self.I+self.m*(self.l**2))-((self.m*self.l)**2)
                #q => setting reocurring constants
                open_loop_transfer_function = control.TransferFunction([((-self.m*self.l)/q)], [1, 0, (((self.M + self.m)*self.g*self.m*self.l)/q)])
                
                kd = 1000 
                kp = -100
                ki = 0

                pid_controller = control.TransferFunction([kd, kp, ki], [1, 0])
                #setting up control function
                transfer_function = (open_loop_transfer_function/(1 + open_loop_transfer_function*pid_controller)) 
                #closed loop = open/(1 + (open*control func))                               
                t, force_array = control.impulse_response(transfer_function, X0 = error)
                #gives an impulse and stores how it responds over time
                #IC = starting angle (error), creates a time array (t) and force array, the latter is the actual system output
                force =  force_array[0]
                #only care about first value as it corresponds to our IC

                return force

        def calculate (self, observation):

                force = self.pid_controller_pendulum(observation)

                if (force >= 0):
                        action = self.make_move_left_action()
                        # sol = self.make_more_....()*force
                elif (force < 0):
                        action = self.make_move_right_action()

                return action 
