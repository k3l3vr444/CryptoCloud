from setuptools import setup

setup(
    name='crypto_cloud',
    version='0.1',
    description='https://cryptocloud.plus/ api',
    author='k3l3vr444',
    author_email='ayukanov.nikita@gmail.com',
    packages=['crypto_cloud'],  # same as name
    install_requires=['pydantic', 'aiohttp'],  # external packages as dependencies
)
