# mirocard-scanner-simulator
A simulator of a [MiroCard](https://mirocard.swiss/) gateway implementing the [CoAP protocol](https://datatracker.ietf.org/doc/html/rfc7252). 

The CoAP API exposes the following observeable resources:
- humidity
- pose
- temperature

By default, upon receiving a request `CoAP GET /<resource>, Observe=0` from a client, the server notifies the client every time the value of the resource changes. 

Simulated samping rates:
- humidity sampling rate: 10s
- pose sampling rate: 10s
- temperature sampling rate: 60s

## Dependencies
- [Python3](https://www.python.org/downloads/)
- [pip3](https://pypi.org/project/pip/)
- [CoAPthon3](https://github.com/Tanganelli/CoAPthon3)

It is recommended to install CoAPthon3 directly from Github:
```
$ git clone https://github.com/Tanganelli/CoAPthon3.git
$ cd CoAPthon3
$ python3 setup.py sdist
$ pip3 install dist/CoAPthon3-1.0.1+fb.[generated_datetime].tar.gz -r requirements.txt
```

Alternatively, you can install CoAPthon3 using pip3:
```
$ pip3 install CoAPthon3
```

## Run the MiroCard gateway CoAP server
Run the simulator:
```
$ python3 coapserver.py
```

## Run an example CoAP client
Run an example client that observes all the resources of the MiroCard gateway:
```
$ python3 coapclient.py
```
Optionally, you can specify which resources the client observes using optional parameters:
- `-hm`, `--humidity`: observe the humidity
- `-p`, `--pose`: observe the pose
- `-t`, `--temperature`: observe the temperature

E.g.:
```
$ python3 coapclient.py --humidity --pose
```
