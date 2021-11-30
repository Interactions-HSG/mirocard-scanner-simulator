import logging
import logging.config
import argparse
import sys
from coapthon.client.helperclient import HelperClient, defines

IP_ADDRESS = "127.0.0.1"
PORT = 5683


# Humidity notification handler
def handle_humidity(response):
    print(f"Notification from /humidity: {response.payload}")


# Pose notification handler
def handle_pose(response):
    print(f"Notification from /pose: {response.payload}")


# Temperature notification handler
def handle_temperature(response):
    print(f"Notification from /temperature: {response.payload}")


def get_args():
    parser = argparse.ArgumentParser(description='app description')
    # Optional positional arguments
    # Observe humidity argument
    parser.add_argument('--humidity', '-hm', action='store_true',
                        help='Observe humidity')
    # Observe pose argument
    parser.add_argument('--pose', '-p', action='store_true',
                        help='Observe pose')
    # Observe temperature argument
    parser.add_argument('--temperature', '-t', action='store_true',
                        help='Observe temperature')

    args = parser.parse_args()
    if not args.humidity and not args.pose and not args.temperature:
        args.humidity = args.pose = args.temperature = True

    logging.info(f"Arguments: \n"
                 f"--humidity, -hm : {args.humidity}\n"
                 f"--pose, -p : {args.pose}\n"
                 f"--temperature, -t : {args.temperature}\n")
    return args


def main():
    try:
        """
            Init a different client for each observed resource
            because HelperClient queue probably does not implement reordering and wrong callbacks are firing
            https://datatracker.ietf.org/doc/html/rfc7641#section-3.4
            Related to closed issue https://github.com/Tanganelli/CoAPthon/issues/88
            """
        # Client list
        clients = []

        # Get arguments
        args = get_args()

        # Observe humidity resource
        if args.humidity:
            logging.info(f"Send OBSERVE /humidity")
            hum_client = HelperClient(server=(IP_ADDRESS, PORT))
            hum_client.observe("/humidity", handle_humidity)
            hum_client.close()
            logging.info("closed")

        # Observe pose resource
        if args.pose:
            logging.info(f"Send OBSERVE /pose")
            pose_client = HelperClient(server=(IP_ADDRESS, PORT))
            pose_client.observe("/pose", handle_pose)

        # Observe temperature resource
        if args.temperature:
            logging.info(f"Send OBSERVE /temperature")
            temp_client = HelperClient(server=(IP_ADDRESS, PORT))
            temp_client.observe("/temperature", handle_temperature)

    except KeyboardInterrupt:
        logging.info("Client Shutdown")
        logging.info("Exiting...")


if __name__ == '__main__':
    logging.config.fileConfig('../logging.conf')
    main()
