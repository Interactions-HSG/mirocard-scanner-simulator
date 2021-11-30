# mirocard-scanner-simulator
A Thing that simulates the behavior of a [miro Card](https://miromico.ch/portfolio/mirocard/?lang=en) gateway.

The Thing provides the following observable properties:
- humidity
- pose
- temperature

## Dependencies
- [Python3](https://www.python.org/downloads/)
- [pip3]
- [CoAPthon3](https://github.com/Tanganelli/CoAPthon3)

It is recommended to install CoAPthon3 directly from Github (requires Git)
```
$ git clone https://github.com/Tanganelli/CoAPthon3.git
$ cd CoAPthon3
$ python3 setup.py sdist
$ sudo pip3 install dist/CoAPthon3-1.0.1+fb.[generated_datetime].tar.gz -r requirements.txt
```

