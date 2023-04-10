# Cyber-Breach-Detector

## Installation instructions
1. Clone the github repository
`git clone https://github.com/initd1/Cyber-Breach-Detector.git`

### Environment Set-up

1. Install python-pip in your environment
2. Install virtualenv
`pip install virtualenv`
3. Create virtual environment
`virtualenv <environment-name>`
4. Activate virutal environment  
`source <environment-name>/bin/activate`(Linux or MacOS users) OR `<environment-name>\Scripts\activate.bat` (windows users)
5. Install required packages in the virtual environment
`pip install -r requirements.txt`


## Prerequisite
1. Ensure `config.ini` file is created under Config directory
2. Format of `config.ini` file is as below:
```config.ini
[APIKeys]
VT_APIKey = 1234567890
HIBP_APIKey = 1234567890
```
3. Add API keys for Virus Total and Haveibeenpwned

## Execution
1. HackAlert Usage:
```
python main.py -h
usage: main.py [-h] [-e EMAIL] [-i IP] [-u USERNAME]

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
![image](https://user-images.githubusercontent.com/90045652/230607374-aaa07b2f-7f45-461d-8a0a-7cf5ac58536c.png)

## Tests

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

