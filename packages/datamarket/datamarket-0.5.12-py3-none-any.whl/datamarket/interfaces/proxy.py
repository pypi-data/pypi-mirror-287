########################################################################################################################
# IMPORTS

import logging
import time

import requests
from stem import Signal
from stem.control import Controller

########################################################################################################################
# CLASSES

logger = logging.getLogger(__name__)
logging.getLogger("stem").setLevel(logging.WARNING)


class ProxyInterface:
    CHECK_IP_URL = "https://wtfismyip.com/json"

    def __init__(self, config):
        if "proxy" in config:
            self.config = config["proxy"]
            self.current_index = 0  # Initialize index for round robin
        else:
            logger.warning("no proxy section in config")

    @property
    def proxies(self):
        return self.get_proxies(use_tor="tor_password" in self.config)

    @staticmethod
    def get_proxy_url(host, port, user=None, password=None, use_socks=True):
        proxy_url = f"{host}:{port}"

        if user and password:
            proxy_url = f"{user}:{password}@{proxy_url}"

        proxy_url = f"socks5://{proxy_url}" if use_socks else f"http://{proxy_url}"
        return proxy_url

    def get_proxies(self, use_tor=True):
        if use_tor:
            proxy_url = self.get_proxy_url("127.0.0.1", 9050)
        else:
            host_port_pairs = [hp.split(":") for hp in self.config["hosts"].split(",")]
            current_host, current_port = host_port_pairs[self.current_index]
            self.current_index = (self.current_index + 1) % len(host_port_pairs)

            user = self.config["user"] if "user" in self.config else None
            password = self.config["password"] if "password" in self.config else None
            use_socks = self.config["socks"].lower() == "true" if "socks" in self.config else False

            proxy_url = self.get_proxy_url(current_host, current_port, user, password, use_socks)

        return {
            "http": proxy_url,
            "https": proxy_url,
        }

    def check_current_ip(self):
        try:
            return requests.get(self.CHECK_IP_URL, proxies=self.proxies).json()[
                "YourFuckingIPAddress"
            ]
        except Exception as ex:
            logger.error(ex)

    def renew_tor_ip(self):
        try:
            logger.info(f"renewing Tor ip: {self.check_current_ip()}...")
            with Controller.from_port(port=9051) as controller:
                controller.authenticate(password=self.config["tor_password"])
                controller.signal(Signal.NEWNYM)

            time.sleep(5)
            logger.info(f"new Tor IP: {self.check_current_ip()}")

        except Exception as ex:
            logger.error("unable to renew Tor ip")
            logger.error(ex)
