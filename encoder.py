import argparse
from tokenize import cookie_re
import helpers.encoder_functions as encoder
import argparse
from helpers.image_textoverlay import draw_nosignal_image
import json
import logging
import sys
logging.basicConfig(stream=sys.stderr, level=logging.INFO)


parser = argparse.ArgumentParser(
    prog='Magewell encoder setup script',
    description='Connect to your magewell encoder and changes some settings and creates a no signal file with its name',
    epilog='Any other ideas for functions, or support needed? Contact Sundgaard')

# the address of the encoder you want to configure
parser.add_argument('--ip', help='Ip adress; example -> --ip 10.10.2.200')
parser.add_argument('--logging', default='INFO',
                    help='Possible logging levels: DEBUG, INFO, WARN, ERROR, CRITICAL')


def app(ip):
    #args = parser.parse_args()
    #ip = args.ip

    headers = encoder.login(ip)
    logging.debug(f"{headers=}")

    response, settings = encoder.get_settings(ip, headers)

    name = settings["name"]

    logging.debug(f"{response=}", f"{name=}")

    filename = draw_nosignal_image(name)

    response = encoder.add_nosignal_file(ip, headers, filename)

    response_code = json.loads(response)["result"]

    if response_code == 0:
        logging.info(f"Updated the no-signal picture of {name}")
        return f"Updated the no-signal picture of {name}"
    if response_code != 0:
        logging.info(
            f"Something went wrong. The errormessage from the magewell was {response_code=}")
        return f"Something went wrong. The errormessage from the magewell was {response_code=}"


if __name__ == '__main__':
    app()
