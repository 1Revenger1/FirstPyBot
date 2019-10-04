from wpilib.command import Command
from chassis import Chassis 

class DriveStraightCommand(Command):

    chassis = Chassis.getInstance()

    def __init__(self, driveDistance):
        self.driveDistance = driveDistance


    def initialize(self):
        self.endPosition = chassis.getPositon() + driveDistance
        self.reverseDirection = chassis.getPosition() > driveDistance

        self.chassis.setPower(-1 if self.reverseDirection else 1, 0)

    def isFinished(self):
        return (self.chassis.getPosition() < self.endPosition) if self.reverseDirection else (self.chassis.getPosition() > self.endPosition)
