import requests

from loguru import logger


class GetSubdomains:
    def __init__(self):
        self.endpoint: str = 'https://api.hackertarget.com/hostsearch/?q='
        self.api_rate_limit_text: str = 'API count exceeded - Increase Quota with Membership'

    @logger.catch
    def get_subdomains(self, domain: str) -> list:
        """
        Method to get the subdomains of a domain
        :param domain: The domain to get the subdomains
        :return: The subdomains of the domain
        """
        self.endpoint += domain
        subdomains_found: list = []

        try:
            response: requests.Response = requests.get(self.endpoint)

        except (KeyError, ValueError, requests.exceptions.RequestException):
            logger.warning(f'Error getting the subdomains of the domain {domain}. Hackertarget API error')
            return []

        for line in response.iter_lines():
            line: list[str] = str(line).split(',')

            # Check if the line is not empty
            if len(line) == 0:
                continue

            value: str = line[0].strip("'b")
            ip: str = line[1].strip("'b")

            if value == self.api_rate_limit_text:
                logger.warning(
                    f'Error getting the subdomains of the domain {domain}. Hackertarget API rate limit exceeded')
                break

            if [value, ip] not in subdomains_found:
                subdomains_found.append([value, ip])

        return subdomains_found
