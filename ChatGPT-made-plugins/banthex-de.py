import os
import logging
import requests
from datetime import datetime
from threading import Lock
from pwnagotchi.utils import StatusFile, remove_whitelisted
from pwnagotchi import plugins
from json.decoder import JSONDecodeError

class Banthex(plugins.Plugin):
    __author__ = 'Your Name'
    __version__ = '1.0.0'
    __license__ = 'GPL3'
    __description__ = 'This plugin automatically uploads handshakes to https://banthex.de'

    def __init__(self):
        self.ready = False
        self.lock = Lock()
        try:
            self.report = StatusFile('/root/.banthex_uploads', data_format='json')
        except JSONDecodeError:
            os.remove("/root/.banthex_uploads")
            self.report = StatusFile('/root/.banthex_uploads', data_format='json')
        self.options = dict()
        self.skip = list()

    def _upload_to_banthex(self, path, timeout=30):
        """
        Uploads the file to https://banthex.de, or another endpoint.
        """
        with open(path, 'rb') as file_to_upload:
            cookie = {'key': self.options['api_key']}
            payload = {'file': file_to_upload}

            try:
                result = requests.post(self.options['api_url'],
                                       cookies=cookie,
                                       files=payload,
                                       timeout=timeout)
                if ' already submitted' in result.text:
                    logging.debug("%s was already submitted.", path)
            except requests.exceptions.RequestException as req_e:
                raise req_e


    def _download_from_banthex(self, output, timeout=30):
        """
        Downloads the results from banthex and safes them to output
        Output-Format: bssid, station_mac, ssid, password
        """
        api_url = self.options['api_url']
        if not api_url.endswith('/'):
            api_url = f"{api_url}/"
        api_url = f"{api_url}?api&dl=1"

        cookie = {'key': self.options['api_key']}
        try:
            result = requests.get(api_url, cookies=cookie, timeout=timeout)
            with open(output, 'wb') as output_file:
                output_file.write(result.content)
        except requests.exceptions.RequestException as req_e:
            raise req_e
        except OSError as os_e:
            raise os_e


    def
