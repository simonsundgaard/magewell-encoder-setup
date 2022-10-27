import json
import logging
import sys
logging.basicConfig(stream=sys.stderr, level=logging.INFO)


def response_code_debug(response):

    response_code = json.loads(response)["result"]

    if response_code == 0:
        logging.debug(f"All good!")
    if response_code != 0:
        logging.debug(
            f"Something went wrong. The errormessage from the magewell was {response_code=}")
