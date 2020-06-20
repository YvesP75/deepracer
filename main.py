import numpy as np
import random


# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# beginning of code

# speed in m/s, and the highest speed possible with the max angle
LOW_SPEED = 1
# speed in m/s on a straight line
MAX_SPEED = 4
# maximum angle in degree
MAX_ANGLE_DEG = 30
# maximum angle in radian
MAX_ANGLE = MAX_ANGLE_DEG * np.pi / 180
# ratio of speed increase
ACCELERATION_COEFF = 0.3
# ratio of speed decrease
DECELERATION_COEFF = 0.2
# a code to say that adherence has been lost
LOST_ADHERENCE = -9999
# in ms
TIMESTEP=0.5

# class track
# lets begin with a simple ellipse
class Track:

    def __init__(self, za, zb, c, width):
        self.za = za
        self.zb = zb
        self.c = c
        self.delta = width / 2

    # determines whether the point is within the track
    def contains(self, z):
        return self.c * (1 - self.delta) < abs(z - self.za) - abs(z - self.zb) < self.c * (1 + self.delta)

    # class segment


# action is a vector (zpoint, i.e. a speed and an angle) of an intention of a movement :
# an action decided by an agent but the outcome is unknown
# and depends on the car caracteristics

class Action:

    def __init__(self, zpoint):
        self.zpoint = zpoint

    def next_position(self, z_origin, zpoint_origin):
        return z_origin+zpoint_origin



# Simplification :
# the car grip is solelely a function of speed
# acceleration : in one step, the car speed increases at the max of : coeff * delta(Vmax-V)
# deceleration : in one step, speed decreases of coeff * V with min  Vmax/coeff2 (and of course can not be zero)

class Car:

    def __init__(self, max_speed):
        self.max_speed=MAX_SPEED
        self.max_angle=MAX_ANGLE
        self.low_speed=LOW_SPEED
        self.acceleration_coeff=ACCELERATION_COEFF
        self.deceleration_coeff = DECELERATION_COEFF


    def get_max_speed(self, angle):
        # if angle == 0 then MAX_SPEED
        # if angle == 30 then LOW_SPEED
        angle = min(30, abs(self.max_speed))
        return self.low_speed + \
               ((self.max_angle - angle) / self.max_angle) * (self.max_speed - self.low_speed)

    # gives the output speed vector (zpoint) given the input (origin) zpoint and the action (the order)
    def get_zpoint(self, zpoint_origin, action):
        speed_origin = abs(zpoint_origin)
        speed_target = abs(action)
        if speed_origin < speed_target: # acceleration
            speed = max (
                speed_origin + (self.max_speed - speed_origin)*self.acceleration_coeff,
                self.max_speed
                         )
            if speed > self.get_max_speed(np.argument(action)):
                return -1 # car has been too fast and lost adherence
        else: # deceleration
            speed = min (
                speed_target,
                speed_origin * (1-self.deceleration_coeff)

            )
        return np.exp(1j * np.argument(action)) * np.argument(zpoint_origin) * speed


# a trunk is possible way to traverse the track. it is defined by an initial position and
# a list of actions (speed vectors)

class Trunk:

    def __init__(self, actions, z0, car, track):
        self.actions = actions
        self.z0 = z0
        self.length = len(self.actions)
        self.positions = self.get_positions()
        self.track = track
        self.car = car

    def get_positions(self):
        z = self.z0
        positions = [z]
        for action in self.actions:
            z = z + self.car.get_zpoint(z, action) * TIMESTEP
            positions.append(z)

    def is_on_track(self):
        on_track = True
        for z in self.positions :
            on_track *= self.track.contains(z)
        return on_track

    def is_on_grip(self):
        return not(isinstance(LOST_ADHERENCE,(self.positions)))

    # returns a modified trunk where speed is incrementallly increased until control loss
    def saturate(self):
        speed_margins = self.get_speed_margins()
        max_speed_margin = max(speed_margins)
        while 0 < max_speed_margin:
            max_speed_margin_index = speed_margins.index(max(speed_margins))
            self.actions *=

    # returns a list for each action how far it is from control loss
    def get_speed_margins(self):
        speed_margins=[]
        for action in self.actions:
            speed_margins.append(
                self.car.get_max_speed(np.angle(action))-abs(action)
            )
        return speed_margins
    #

class TrunkPopulation:

    def __init__(self, trunks):
        self.trunks = trunks
        self.lengths = [len(trunk) for trunk in self.trunks]
        self.actions = self.get_actions()
        self.action_range = []

    # creates a new population which inherits from self properties
    def generate_pop(self, trunks):
        pop = TrunkPopulation(trunks)

    # get the
    def get_actions(self):



    def next_gen(self):
        return \
            self.die_gen(self.mutate_gen(self.cross_gen()))

    def cross_gen(self):
        next_gen = []
        for _ in self.trunks:
            parents = random.choices(self.trunks, weight=np.exp(self.lengths),k=2)
            break_index = random.randint(1, min(min(len(parents[0]), len(parents[1]))-2, 1))
            next_gen.append(np.concatenate((parents[0][0:break_index], parents[1][break_index:])))
            next_gen.append(np.concatenate((parents[1][0:break_index], parents[0][break_index:])))
        return TrunkPopulation(concatenate((self.trunks, next_gen))

    def mutate_gen(pop):
        mutations = random.choices(pop, k=min(int(len(pop.trunks)*MUTATION_RATIO), 2))
        for trunk in mutations:
            mutation_index = random.randint(1,trunk.length)
            trunk[mutation_index] = random.choices(self.actions, 1)
            pop.trunks.append(trunk)
        return pop

    def die_gen(pop):
        deads = random.choices(
            pop,
            weight=1/np.exp(pop.lengths),
            k=