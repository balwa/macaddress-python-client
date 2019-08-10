# MAC Address Vendor lookup CLI

This simple python script can be used to query [https://macaddress.io/](https://macaddress.io/) to get vendor related information about a device MAC Address

## Getting Started

This scripting utility has be written using the standard library included in python 3.x All you need to get started is sign up for an account [here](https://macaddress.io/signup) and obtain your API key.

### Prerequisites

You need a standard installation of Python3 that can be obtained [here](https://www.python.org/downloads/)

### Usage

Export the API key as an environment variable `MACADDRESSIO_API_KEY` before running the script

On linux and MacOS

Example:

```bash
export MACADDRESSIO_API_KEY=at_VKIvhPfcPffhywNDMx61r0E1gAhKW
```

Note the above string is a randomly generated value and if you copy paste this exactly it will result in `"error": "Access restricted. Enter the correct API key."`

And then simply run

```bash
./mac_vendor.py -m "E8404079C860"
```

This should give output of the company name. For the above example it would show:

```bash
Cisco Systems, Inc
```

You can control the output format and 

### Code formatting

Code formatting has be done using [black](https://github.com/psf/black). I really like the philosophy of `gofmt` on which black is based.


## Running with Docker

For your convenience a Dockerfile has also been provided along with the code. Either build it yourself or you can use the one below:

```bash
docker run
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
