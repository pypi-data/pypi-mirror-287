from setuptools import setup, find_packages

setup(
    name='airporticao',
    version='0.1.2',
    description='get details about an airport by its ICAO code',
    url='https://github.com/rtphokie/airporticao.git',
    author='Tony Rice',
    author_email='05hosts_crew@icloud.com',
    license='MIT',
    packages=find_packages(),
    install_requires=['requests-cache', 'timezonefinder', 'bs4'],
    zip_safe=False
)
