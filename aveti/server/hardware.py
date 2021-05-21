"""
hardware.py
Hardware Interface.
"""

__author__      = "Prakash Manandhar"
__copyright__ = "Prakash Manandhar"
__credits__ = ["Prakash Manandhar"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Prakash Manandhar"
__email__ = "prakashm@alum.mit.edu"
__status__ = "Production"

import configparser

config = configparser.ConfigParser()
config.read('server_config.ini')

from . import rpi_hardware

class HardwareFactory:
    rpi = None
    
    @classmethod
    def getRPi(cls):
        if cls.rpi is None:
            if config.getboolean('Operating System', 'RunningInRPi'):
                cls.rpi = rpi_hardware.RPiHardware()
            else:
                cls.rpi = rpi_hardware.MockRPiHardware()
        return cls.rpi