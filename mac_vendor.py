#!/usr/bin/env python3
import argparse
import logging
import os
import re
import sys
import urllib.request

logging.basicConfig(
    level=logging.WARN,
    format="%(levelname)s %(asctime)s %(message)s",
    handlers=[logging.FileHandler("mac_vendor.log"), logging.StreamHandler()],
)


def validate_macaddress(mac_address):
    """Simple function to validate mac address
    
    :param mac_address: input MAC address
    :type mac_address: str
    :return: True if valid format
    :rtype: bool
    """
    return re.match("^([0-9A-Fa-f]{2}[:.-]?){5}([0-9A-Fa-f]{2})$", mac_address.strip())


def request_builder(mac_address, api_key):
    req_url = "https://api.macaddress.io/v1"
    query_params = {"output": "json", "search": mac_address}
    encoded_url = "{0}?{1}".format(req_url, urllib.parse.urlencode(query_params))
    auth_header = {"X-Authentication-Token": api_key}
    req = urllib.request.Request(encoded_url, headers=auth_header)
    return req


def request_sender(request):
    """Returns a string of response obtained from the request
    
    :param request: request URL object
    :type request: urllib.request.Request
    :return: response json output
    :rtype: string
    """
    try:
        response = urllib.request.urlopen(request)
        output = response.read().decode("utf-8")
        return output
    except urllib.error.HTTPError:
        logging.error(
            "status code:{0} message:{1}".format(response.status, response.msg)
        )
        exit(response.status)
    finally:
        response.close()


def formatted_output(response, query_fields, output_type):
    return ""


def main():
    """Main function
    """

    # Setup commandline parser
    parser = argparse.ArgumentParser(
        description="Query macaddress.io and fetch the vendor information associated with the mac address"
    )

    parser.add_argument("macaddr", type=str, help="MAC Address of the device")
    parser.add_argument(
        "-o",
        "--output",
        help="output format control, accepted values are json, csv, minimal",
        dest="output",
        default="minimal",
    )
    parser.add_argument(
        "-q",
        "--query",
        help="query fields, one or multiple comma seperated name,transmission,valid,registered",
        dest="query",
        default="name,",
    )
    parser.add_argument(
        "-r",
        "--rawjson",
        help="return raw json from the server that can be piped to jq for other fields",
        action="store_true",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        help="make output more verbose sets to DEBUG",
        action="store_true",
    )

    args = parser.parse_args()
    mac_address = args.macaddr
    query_fields = args.query
    output_type = args.output

    try:
        api_key = os.environ["MACADDRESSIO_API_KEY"]
    except KeyError:
        logging.error("Please set the environment variable MACADDRESSIO_API_KEY")
        sys.exit(1)
    if not validate_macaddress(mac_address):
        logging.error("Could not validate mac_address")
        sys.exit(1)
    response = request_sender(request_builder(mac_address, api_key))
    if args.rawjson:
        print(response)
        sys.exit(0)
    print(formatted_output(response, query_fields, output_type))


if __name__ == "__main__":
    main()
