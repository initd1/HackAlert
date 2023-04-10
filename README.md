# HackAlert

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
![image](https://user-images.githubusercontent.com/90045652/230607374-aaa07b2f-7f45-461d-8a0a-7cf5ac58536c.png)


