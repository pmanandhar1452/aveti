"""
RPiHardware.py
Hardware Interface and Mock Layers for RPi.
"""

from abc import ABC, abstractmethod
import configparser

config = configparser.ConfigParser()
config.read('server_config.ini')
if config.getboolean('Operating System', 'RunningInRPi'):
    from gpiozero import PWMLED
    from gpiozero import CPUTemperature

class MockRPiPin:
    pass

class AbstractRPiHardware(ABC):
    @abstractmethod
    def connect_triac_pin(self, pin_number):
        return MockRPiPin()

    def get_cpu_temperature(self):
        return -300.0

class MockRPiHardware(AbstractRPiHardware):
    def connect_triac_pin(self, pin_number):
        return MockRPiPin()

class RPiHardware(AbstractRPiHardware):
    def connect_triac_pin(self, pin_number):
        return PWMLED(pin_number)

    def get_cpu_temperature(self):
        return CPUTemperature().temperature