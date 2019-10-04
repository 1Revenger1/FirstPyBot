import wpilib.command as wpilib
from wpilib.smartdashboard import SmartDashboard
import ctre
import robotmap
import math
import chassis.teleopDriveCommnad as TeleopDriveCommnad

class Chassis(wpilib.Subsystem):

    DIAMETER = 6 / 12 # 6 inches converted into 1/2 foot
    CIRCUMFERENCE = DIAMETER * math.pi
    TICKS_TO_ROTATIONS = 1 / (4096) # 4096 ticks in mag encoders
    ROTATIONS_TO_FEET = TICKS_TO_ROTATIONS * CIRCUMFERENCE

    __instances = None

    def __init__(self):
        self.leftMaster = ctre.TalonSRX(robotmap.LEFT_DRIVE_MASTER)
        self.leftSlave = ctre.VictorSPX(robotmap.LEFT_DRIVE_SLAVE)
        self.rightMaster = ctre.TalonSRX(robotmap.RIGHT_DRIVE_MASTER)
        self.rightSlave = ctre.VictorSPX(robotmap.RIGHT_DRIVE_SLAVE)

        self.rightTalon.setInverted(True)

        self.leftTalon.configSelectedFeedbackSensor(ctre.FeedbackDevice.CTRE_MagEncoder_Relative, 0, 0)
        self.rightTalon.configSelectedFeedbackSensor(ctre.FeedbackDevice.CTRE_MagEncoder_Relative, 0, 0)

        self.leftSlave.follow(leftMaster)
        self.rightSlave.follow(rightMaster)

    @staticmethod
    def getInstance() -> Chassis:
        if Chassis.__instance == None:
            Chassis()
        return Chassis.__instance

    def initDefaultCommand(self):
        self.setDefaultCommand(TeleopDriveCommnad())

    def __setLeftRightPower(self, left, right):
        self.leftMaster.set(ctre.ControlMode.PercentOutput, left)
        self.rightMaster.set(ctre.ControlMode.PercentOutput, right)

    def setPower(self, forward, rotational):
        self.__setLeftRightPower((forward + rotational), (forward - rotational))

    def getVelocity(self):
        leftVelocity = self.leftMaster.getSelectedSensorVelocity() * ROTATIONS_TO_FEET
        rightVelocity = self.rightMaster.getSelectedSensorVelocity() * ROTATIONS_TO_FEET
        return (leftVelocity + rightVelocity) / 2

    def periodic(self):
        SmartDashboard.putNumber("Velocity", self.getVelocity())
