import json
import logging

from coapthon import defines
from coapthon.resources.resource import Resource


class PoseResource(Resource):
    def __init__(self, name="PoseResource", coap_server=None):
        super(PoseResource, self).__init__(name, coap_server, visible=True,
                                           observable=True, allow_children=False)

        self.resource_type = "pose"
        self.content_type = "application/json"
        self.value = 0
        self.min_value = 0
        self.max_value = 4
        self.type = int

    def render_GET(self, request):
        logging.info(f"GET /{self.resource_type}")
        self.payload = (defines.Content_types["application/json"], json.dumps({"value": self.value}))
        return self

    def render_PUT(self, request):
        logging.info(f"PUT /{self.resource_type}")
        self.value = request.payload
        return self


class HumidityResource(Resource):
    def __init__(self, name="HumidityResource", coap_server=None):
        super(HumidityResource, self).__init__(name, coap_server, visible=True,
                                               observable=True, allow_children=False)

        self.resource_type = "humidity"
        self.content_type = "application/json"
        self.value = 15.00
        self.min_value = 15.00
        self.max_value = 40.00
        self.type = float

    def render_GET(self, request):
        logging.info(f"GET /{self.resource_type}")
        self.payload = (defines.Content_types["application/json"], json.dumps({"value": self.value}))
        return self

    def render_PUT(self, request):
        logging.info(f"PUT /{self.resource_type}")
        self.value = request.payload
        return self


class TemperatureResource(Resource):
    def __init__(self, name="TemperatureResource", coap_server=None):
        super(TemperatureResource, self).__init__(name, coap_server, visible=True,
                                                  observable=True, allow_children=False)

        self.resource_type = "temperature"
        self.content_type = "application/json"
        self.value = 10.00
        self.min_value = 10.00
        self.max_value = 26.00
        self.type = float

    def render_GET(self, request):
        logging.info(f"GET /{self.resource_type}")
        self.payload = (defines.Content_types["application/json"], json.dumps({"value": self.value}))
        return self

    def render_PUT(self, request):
        logging.info(f"PUT /{self.resource_type}")
        self.value = request.payload
        return self
