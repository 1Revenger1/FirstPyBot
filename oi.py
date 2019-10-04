from wpilib import XboxController
from wpilib.buttons import JoystickButton
from wpilib.interfaces import GenericHID
import math
from chassis.driveStraightCommand import DriveStraightCommand

class OI():

    __instances = None

    DEADZONE = 1/128

    def __init__(self):
        self.driverController = XboxController(0)
        self.manipulatorController = XboxController(1)

        self.aButtonDriver = JoystickButton(self.driverController, 0)

        self.aButtonDriver.whenPressed(DriveStraightCommand(10))

    @staticmethod
    def getInstance() -> OI:
        if(OI.__instances == None):
            OI.__instances = OI()
        return OI.__instances

    def __deadzone(self, input, deadzone=DEADZONE) -> Number:
        absValue = math.fabs(input)
        # no signum ;-;
        return 0 if abs < deadzone else ((absValue - deadzone) / (1.0 - deadzone) * math.copysign(1, input))

    def getLeftY(self):
        return self.__deadzone(self.driverController.getY(GenericHID.Hand.kLeft))
    
    def getRightY(self):
        return self.__deadzone(self.driverController.getY(GenericHID.Hand.kRight))
