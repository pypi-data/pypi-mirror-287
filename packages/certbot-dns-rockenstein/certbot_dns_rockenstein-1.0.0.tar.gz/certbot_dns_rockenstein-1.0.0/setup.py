from setuptools import setup, find_packages

setup(
    name='certbot-dns-rockenstein',
    version='1.0.0',
    description="rockenstein DNS Authenticator plugin for Certbot",
    url='https://www.rockenstein.de',
    author="Frank Mueller",
    author_email='fm@rockenstein.de',
    install_requires=[
        'certbot',
        'requests'
    ],
    entry_points={
        'certbot.plugins': [
            'dns-rockenstein = certbot_dns_rockenstein._internal.dns_rockenstein:Authenticator'
        ],
    },
    packages=find_packages(),
)
