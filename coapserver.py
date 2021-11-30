import logging
import logging.config
import random
import threading
from datetime import timedelta

from coapthon.server.coap import CoAP

from coapresources import PoseResource, HumidityResource, TemperatureResource

IP_ADDRESS = "127.0.0.1"
PORT = 5683
SIM_POSE_SAMPLING_RATE = 10
SIM_HUMIDITY_SAMPLING_RATE = 10
SIM_TEMP_SAMPLING_RATE = 60


class ScannerSimulator:
    pass


class CoAPServer(CoAP):
    def __init__(self, host, port):
        CoAP.__init__(self, (host, port))

        # Init resources
        self.pose_resource = PoseResource(coap_server=self)
        self.humidity_resource = HumidityResource(coap_server=self)
        self.temperature_resource = TemperatureResource(coap_server=self)

        # Add resources to the server
        self.add_resource('pose/', self.pose_resource)
        self.add_resource('humidity/', self.humidity_resource)
        self.add_resource('temperature/', self.temperature_resource)

        # Set scanner simulators for resources.
        pose_sampling = ScannerSimulator(self.pose_resource,
                                         interval=timedelta(seconds=SIM_POSE_SAMPLING_RATE),
                                         execute=self.simulate_discovery)

        humidity_sampling = ScannerSimulator(self.humidity_resource,
                                             interval=timedelta(seconds=SIM_HUMIDITY_SAMPLING_RATE),
                                             execute=self.simulate_discovery)

        temperature_sampling = ScannerSimulator(self.temperature_resource,
                                                interval=timedelta(seconds=SIM_TEMP_SAMPLING_RATE),
                                                execute=self.simulate_discovery)

        # Start scanner simulators
        pose_sampling.start()
        humidity_sampling.start()
        temperature_sampling.start()

    # Simulate an observation
    def simulate_discovery(self, resource, value):
        resource.value = value
        self.notify(resource)
        resource.observe_count += 1
        logging.info(f"Change of {resource.name} value detected: {resource.value}")


# Simulate bluepy.btle.Scanner for generating incoming data.
class ScannerSimulator(threading.Thread):
    def __init__(self, resource, interval, execute):
        threading.Thread.__init__(self)

        self.daemon = True
        self.stopped = threading.Event()
        self.resource = resource
        self.interval = interval
        self.execute = execute

    def stop(self):
        self.stopped.set()
        self.join()

    def run(self):
        while not self.stopped.wait(self.interval.total_seconds()):
            if self.resource.type == int:
                scanned_value = random.randint(self.resource.min_value, self.resource.max_value)
            elif self.resource.type == float:
                scanned_value = round(random.uniform(self.resource.min_value, self.resource.max_value), 2)
            else:
                continue
            logging.info(f"Scanned a {self.resource.name} value: {scanned_value}")
            self.execute(self.resource, scanned_value)


def main():
    # Start the server
    server = CoAPServer(IP_ADDRESS, PORT)
    logging.info(f"CoAP server start on {server.server_address}" )

    try:
        logging.info("Server Listening")
        server.listen(10)
    except KeyboardInterrupt:
        logging.info("Server Shutdown")
        server.close()
        logging.info("Exiting...")


if __name__ == '__main__':
    logging.config.fileConfig('logging.conf')
    main()
