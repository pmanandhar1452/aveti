"""
RPiHardware.py
Hardware Interface and Mock Layers for RPi.
"""

from abc import ABC, abstractmethod
import configparser, threading, time

config = configparser.ConfigParser(
    converters={'list': lambda x: [i.strip() for i in x.split(',')]})
config.read('server_config.ini')
if config.getboolean('Operating System', 'RunningInRPi'):
    from gpiozero import CPUTemperature, Buzzer
    import Adafruit_DHT

class MockRPiPin:
    pass

class AbstractRPiHardware(ABC):
    def get_cpu_temperature(self):
        return -300.0

    def _connect_plants(self):
        self.plant_names = []
        self.temp_rh_pins = []
        self.relay_pins = []
        plant_settings = config.getlist("Plants", "Plant1")
        self.plant_names.append(plant_settings[1])
        self.temp_rh_pins.append(plant_settings[-2])
        self.relay_pins.append(plant_settings[-1])

    def get_plants(self):
        return self.plant_names

    def get_temp_rh(self, plant_id):
        sensor_readings = {
                    "timestamp_s": time.time(),
                    "temp_degC": 0.0,
                    "rh_percent": 0.0,
                } 
        return sensor_readings

    def water_plant(self):
        pass

class MockRPiHardware(AbstractRPiHardware):
    pass

class TempRHThread(threading.Thread):

    def __init__(self, gpio_pin):
        threading.Thread.__init__(self)
        self.stopped = True
        self.sensor_readings = {
                "timestamp_s": 0.0,
                "temp_degC": 0.0,
                "rh_percent": 0.0,
            } 
        self.sensor = Adafruit_DHT.DHT22
        self.tS_s = config.getfloat('Control', 'tS_s')
        self.gpio_pin = gpio_pin

    def run(self):
        self.stopped = False
        while not self.stopped:
            loop_start = time.time()
            humidity, temperature = Adafruit_DHT.read_retry(
                self.sensor, self.gpio_pin)
            timestamp = time.time()
            self.sensor_readings["timestamp_s"] = timestamp
            self.sensor_readings["temp_degC"] = temperature
            self.sensor_readings["rh_percent"] =  humidity
            loop_end = time.time()
            delta_time = loop_end - loop_start
            if (delta_time < self.tS_s):
                time.sleep(self.tS_s - delta_time)
            
    def stop(self):
        self.stopped = True

class RPiHardware(AbstractRPiHardware):

    def __init__(self):
        self._connect_plants()
        self.temp_rh_threads = []
        self.water_relays = []
        for i in range(len(self.plant_names)):
            print("Here")
            rh_thread = TempRHThread(self.temp_rh_pins[i])
            self.temp_rh_threads.append(rh_thread) 
            rh_thread.start()

            self.water_relays.append(Buzzer(self.relay_pins[i]))
            self.water_relays[i].off()

    def get_temp_rh(self, plant_id):
        return self.temp_rh_threads[plant_id].sensor_readings
        
    def get_cpu_temperature(self):
        return CPUTemperature().temperature

    def water_plant(self):
        pass
