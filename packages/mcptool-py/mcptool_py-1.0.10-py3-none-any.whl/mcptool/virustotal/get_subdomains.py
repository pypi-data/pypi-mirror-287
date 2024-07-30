import socket

import requests
from ezjsonpy import get_config_value
from loguru import logger


class GetSubdomains:
    def __init__(self):
        self.endpoint: str = 'https://www.virustotal.com/vtapi/v2/domain/report'
        self.params: dict = {
            'apikey': get_config_value('virusTotalApiKey'),
            'domain': ''
        }

    @logger.catch
    def get_subdomains(self, domain: str) -> list:
        """
        Get the subdomains of a domain using the VirusTotal API
        :param domain: The domain to get the subdomains from
        :return: A list of subdomains
        """
        self.params['domain'] = domain
        subdomains_found: list = []

        try:
            response: requests.Response = requests.get(self.endpoint, params=self.params)
            subdomains: list = sorted(response.json()['subdomains'])

        except (KeyError, ValueError, requests.exceptions.RequestException):
            logger.warning(f'Error getting the subdomains of the domain {domain}. VirusTotal API error')
            return []

        for subdomain in subdomains:
            if subdomain not in [item[0] for item in subdomains_found]:
                try:
                    ip = socket.gethostbyname(subdomain)

                    if [subdomain, ip] not in subdomains_found:
                        subdomains_found.append([subdomain, ip])

                except (socket.gaierror, socket.error):
                    pass

        return subdomains_found
