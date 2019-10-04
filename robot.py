from wpilib.command import Scheduler 
from chassis import Chassis

class PracticeBot(sea.GeneratorBot):
    
    def __init__(self):
        super(self)
        self.chassis = Chassis.getInstance()

    def teleop(self):
        while True:

            # Run periodic methods in subsystems and run all currently queued Commands
            Scheduler.run()
            yield
