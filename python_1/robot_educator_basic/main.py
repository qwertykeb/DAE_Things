#!/usr/bin/env pybricks-micropython

"""
LEGO® MINDSTORMS® EV3 Robot Educator Driving Base Program with Infrared Sensor
-----------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
"""

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, InfraredSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Initialize the EV3 Brick and devices.
ev3_brick = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
infrared_sensor = InfraredSensor(Port.S4)

# Constants for the robot's physical dimensions
AXLE_TRACK = 104         # Distance between the wheels in mm
WHEEL_DIAMETER = 55.5    # Diameter of the wheels in mm

# Initialize the drive base with the two motors
robot_drive_base = DriveBase(left_motor, right_motor, wheel_diameter=WHEEL_DIAMETER, axle_track=AXLE_TRACK)

# List of target distances to iterate over, representing different obstacles in cm.
target_distances = [20, 25, 30, 35]

# Other variables of different data types
robot_name = "EV3Bot"  # String data type representing the robot's name
initial_speed = 100    # Integer representing the robot's initial speed in mm/s
speed_factor = 1.5     # Float representing a factor to increase speed

def check_distance_and_move(target_distance):
    """
    Checks the IR sensor's distance and controls robot movement based on the target distance.

    Args:
        target_distance (int): Distance threshold in cm for IR sensor.
    """
    # Read current distance to the nearest object
    current_distance = infrared_sensor.distance()

    # Decision-making structure to determine movement based on distance
    if current_distance < target_distance:
        robot_drive_base.straight(500)  # Move forward by 500 mm if object is close
        ev3_brick.speaker.beep()  # Sound to indicate movement
    else:
        # If no object is detected nearby, move backward and turn
        robot_drive_base.straight(-500)  # Move backward by 500 mm
        ev3_brick.speaker.beep()
        robot_drive_base.turn(360)       # Turn clockwise by 360 degrees
        ev3_brick.speaker.beep()
        robot_drive_base.turn(-360)      # Turn counterclockwise back to original orientation
        ev3_brick.speaker.beep()

def run_robot():
    """
    Main function to iterate over target distances and apply check_distance_and_move() for each.
    """
    # Iterate over each distance in the list of target distances
    for distance in target_distances:
        check_distance_and_move(distance)  # Call custom function for each distance
        wait(500)  # Small delay to allow for controlled movement

# Start the robot program by calling the main function
run_robot()
