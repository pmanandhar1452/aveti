"""
RPiHardware.py
Hardware Interface and Mock Layers for RPi.
"""

from abc import ABC, abstractmethod
import configparser

config = configparser.ConfigParser()
config.read('server_config.ini')
if config.getboolean('Operating System', 'RunningInRPi'):
    from gpiozero import CPUTemperature

class MockRPiPin:
    pass

class AbstractRPiHardware(ABC):
    def get_cpu_temperature(self):
        return -300.0

    def connect_plants(self):
        pass

    def get_plants(self):
        pass

class MockRPiHardware(AbstractRPiHardware):
    pass

class RPiHardware(AbstractRPiHardware):
        
    def get_cpu_temperature(self):
        return CPUTemperature().temperature

    def connect_plants(self):
        pass