from setuptools import setup, find_packages

setup(
    name='MQTTSimpleClient',
    version='0.1.0',
    description='A custom MQTT library for interaction with a broker',
    author='Riccardo Filomena',
    author_email='filomena.riccardo@gmail.com',
    packages=find_packages(),
    install_requires=[
        'paho-mqtt',
        'lxml',
        'setuptools'
        # aggiungi altre dipendenze qui
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
