from wpilib.command import Command
import ctre
import math
from chassis import Chassis
from oi import OI

class TeleopDriveCommand(Command):

    def __init__(self):
        self.requires(Chassis.getInstance())

    def execute(self):
        leftInput = OI.getInstance().getLeftY()
        rightInput = OI.getInstance().getRightY()

        forwardSpeed = self.__desensitize((leftInput + rightInput) / 2)
        rotationalSpeed = self.__desensitize((leftInput - rightInput) / 2, 3)

        Chassis.getInstance().setPower(forwardSpeed, rotationalSpeed)

    def __desensitize(self, input, power=2) -> Number:
        return math.fabs(input ** (power - 1)) * input
        

    def isFinished(self):
        return False