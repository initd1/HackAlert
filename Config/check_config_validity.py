import configparser

config = configparser.ConfigParser()

def read_config():
    return config.read('Config/logger.ini')



# check if the required sections are present
if 'loggers' not in config.sections() or 'handlers' not in config.sections():
    raise ValueError('Missing required section in config.ini')

if 'keys' not in config['loggers'] or 'suspicious' not in config['loggers']:
    raise ValueError('Missing required key in loggers section in config.ini')

# check if the required keys are present in the 'handlers' section
if 'keys' not in config['handlers'] or 'console' not in config['handlers']['keys']:
    raise ValueError('Missing required key in handlers section in config.ini')

# check if the values of the keys are in the expected format
if not isinstance(config.getint('handlers', 'console.level'), int):
    raise ValueError('Invalid value for console.level in config.ini')

if not isinstance(config.getint('loggers', 'keys.suspicious.level'), int):
    raise ValueError('Invalid value for keys.suspicious.level in config.ini')

if __name__ == "__main__":
    read_config()
