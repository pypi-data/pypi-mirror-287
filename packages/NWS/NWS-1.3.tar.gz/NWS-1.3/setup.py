from setuptools import setup, find_packages

setup(
    name='NWS',
    version='1.3',
    packages=find_packages(),
    install_requires = [
        "requests"
    ],
    author="Programer-Turtle",
    description="A module that uses the National Weather Service's API to get weather data meaning no need for an account, or API token.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown"
)