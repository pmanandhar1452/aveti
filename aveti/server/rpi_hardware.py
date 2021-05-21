"""
RPiHardware.py
Hardware Interface and Mock Layers for RPi.
"""

from abc import ABC, abstractmethod
import configparser

config = configparser.ConfigParser()
config.read('server_config.ini')
if config.getboolean('Operating System', 'RunningInRPi'):
    from gpiozero import CPUTemperature, Buzzer
    

class MockRPiPin:
    pass

class AbstractRPiHardware(ABC):
    def get_cpu_temperature(self):
        return -300.0

    def connect_plants(self):
        pass

    def get_plants(self):
        pass

    def water_plant(self):
        pass

class MockRPiHardware(AbstractRPiHardware):
    pass

class RPiHardware(AbstractRPiHardware):
        
    def __init__(self):
        self.bzon = False
        self.bz = Buzzer(26)
        self.bz.off()
        
    def get_cpu_temperature(self):
        return CPUTemperature().temperature

    def connect_plants(self):
        pass

    def water_plant(self):
        if self.bzon:
            self.bz.off()
        else:
            self.bz.on()
        self.bzon = not self.bzon
