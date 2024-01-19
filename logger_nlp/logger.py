from datetime import datetime
import logging
import configuration.environment_config as env_config
import sys

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class NLPLogger(metaclass=Singleton):
    def __init__(self):
        logging.basicConfig(stream=sys.stdout, filemode='w', level=logging.DEBUG)
        self.logger = logging.getLogger(env_config.fluent_logname)

    def debug(self, text, func=""):
        self.logger.debug(self._create_response_dict(text, func))

    def warn(self, text, func=""):
        self.logger.warning(self._create_response_dict(text, func))
    
    def error(self, text, func=""):
        self.logger.error(self._create_response_dict(text, func))
    
    def info(self, text, func=""):
        self.logger.info(self._create_response_dict(text, func))

    def _create_response_dict(self, text, func=""):
        return {
            'ts': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3],
            'function': func,
            'msg': text
        }