from typing import Iterable, Type, Any
import acme.challenges
from acme.challenges import Challenge
from certbot.plugins import dns_common
from .rox_api import RoxApi


class Authenticator(dns_common.DNSAuthenticator):
    description = "Obtain certificates using a DNS TXT record (if you are using rockenstein AG " \
                  "for DNS). "

    def _perform(self, domain: str, validation_name: str, validation: str) -> None:
        url = self.conf('url')
        if self.credentials.conf('url'):
            url = self.credentials.conf('url')

        self._roxApi = RoxApi(self.credentials.conf('token'), url, not self.conf('ignore-ssl'))

        # domains can be subdomains, eg. "abc.example.com" so we have to find out
        # the base domain name
        basedomain = self._roxApi.get_base_domain(domain)

        # make dns entry
        self._roxApi.add_txt_record(basedomain + '.',
                                    validation_name + '.',
                                    validation)

    def _cleanup(self, domain: str, validation_name: str, validation: str) -> None:
        # domains can be subdomains, eg. "abc.example.com" so we have to find out
        # the base domain name
        basedomain = self._roxApi.get_base_domain(domain)

        # delete dns entry
        self._roxApi.del_txt_record(basedomain + '.',
                                    validation_name + '.',
                                    validation)

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    @classmethod
    def add_parser_arguments(cls, add, **kwargs) -> None:
        super().add_parser_arguments(
            add, default_propagation_seconds=120
        )
        add("url", help="URL for rockenstein API", default="https://api.rox.net")
        add("ignore-ssl", action="store_true", default=False)
        add("credentials", help="rockenstein AG credentials INI file")

    def _setup_credentials(self):
        self.credentials = self._configure_credentials(
            "credentials",
            "rockenstein AG credentials INI file",
            {
                "token": "Generated token from rockenstein AG"
            }
        )

    def more_info(self) -> str:
        return self.description

    def get_chall_pref(self, domain: str) -> Iterable[Type[Challenge]]:
        return [
            acme.challenges.DNS01
        ]
