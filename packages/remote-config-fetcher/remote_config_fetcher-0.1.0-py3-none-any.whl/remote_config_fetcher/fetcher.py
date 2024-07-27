import logging
import firebase_admin
from firebase_admin import credentials
from firebase_admin import remote_config


class RemoteConfigFetcher:
    def __init__(self, credential_path: str):
        self.credential_path = credential_path
        self.__initialize_app()

    def __initialize_app(self):
        cred = credentials.Certificate(self.credential_path)
        firebase_admin.initialize_app(cred)

    def get_remote_config_values(self):
        try:
            template = remote_config.get_template()
            config_values = {key: parameter.default_value for key,
                             parameter in template.parameters.items()}
            return config_values
        except Exception as e:
            logging.error(f'Error obtaining config values: {e}')
            return None
