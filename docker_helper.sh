#!/bin/sh

display_usage() { 
	echo 'This container has to be run using docker run --env MACADDRESSIO_API_KEY=key <image_name> mac_vendor.py <MAC_ADDRESS> <OPTIONAL_PARAMS>'
	echo 'Example: docker run --env MACADDRESSIO_API_KEY=$MY_API_KEY github.com/balwa/macaddress-python-client:latest mac_vendor.py E8-40-40-79-C8-60'
    echo 'See Usage: docker run github.com/balwa/macaddress-python-client:latest mac_vendor.py -h'
	}
display_usage