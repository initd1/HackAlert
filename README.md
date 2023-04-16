<p align="center"><img src=https://user-images.githubusercontent.com/90045652/232296629-b5dbaa71-761f-4195-a39e-03108f89bc52.png></p>
<p align="center"><img src="https://user-images.githubusercontent.com/90045652/232291714-09f96b51-a315-4f3e-80df-a386d4e4e98b.png" width="500"/><p>

  
[![Build and Test](https://github.com/initd1/HackAlert/actions/workflows/auto-build-test.yml/badge.svg)](https://github.com/initd1/HackAlert/actions/workflows/auto-build-test.yml)
[![Docker Integration](https://github.com/initd1/HackAlert/actions/workflows/docker-integration.yml/badge.svg)](https://github.com/initd1/HackAlert/actions/workflows/docker-integration.yml)
[![CodeQL](https://github.com/initd1/HackAlert/actions/workflows/github-code-scanning/codeql/badge.svg?branch=main)](https://github.com/initd1/HackAlert/actions/workflows/github-code-scanning/codeql)
![GitHub Repo stars](https://img.shields.io/github/stars/initd1/HackAlert?style=social)
[![Twitter Follow](https://img.shields.io/twitter/follow/initd15?style=social)](https://twitter.com/initd15)

## Installation instructions
1. Clone the github repository
`git clone https://github.com/initd1/HackAlert.git`

## Environment Set-up

1. Install python-pip in your environment
2. Install virtualenv
`pip install virtualenv`
3. Create virtual environment
`virtualenv <environment-name>`
4. Activate virutal environment  
__Mac or Linux__
```bash
source <environment-name>/bin/activate
```
__Windows__
```bash
<environment-name>\Scripts\activate.bat
```

5. Install required packages in the virtual environment
```python
pip install -r requirements.txt
```

## Prerequisites
1. Ensure `config.ini` file is created under Config directory
2. Format of `config.ini` file is as below:
```ini
[APIKeys]
VT_APIKey = 1234567890
HIBP_APIKey = 1234567890
```
3. Add API keys for Virus Total and Haveibeenpwned

## Testing

It is important that before you do anything you have the `requirements.txt` file
installed as it is required for the dependencies that are used in this project.

To install all dependencies listed in this file, run the following:

```bash
python -m pip install -r requirements.txt
```

To execute tests, please ensure that you have the `pytest` module installed.
The unittest module is used, however, this is native to python and does not have to be installed.
To run tests, please ensure that you are in the base directory, where `Tests` and `main.py` is visible.

To run tests with print output:
```bash
pytest -s 
```

To run tests without print output:
```bash
pytest
```
> **Warning** pytest will not run if python site-packages are not already in your global path!

## Execution
1. HackAlert Usage:
```bash
python hackalert.py -h
usage: hackalert.py [-h] [-e EMAIL] [-i IP] [-u USERNAME]

Check if the given data has been compromised in a data breach.

options:
  -h, --help            show this help message and exit
  -e EMAIL, --email EMAIL
                        Email address to check
  -i IP, --ip IP        IP address to check
  -u USERNAME, --username USERNAME
                        Username to check
```

2. Example Usage:
![image](https://user-images.githubusercontent.com/90045652/231768992-80b71df7-b45c-4557-937a-8b46b8274086.png)



