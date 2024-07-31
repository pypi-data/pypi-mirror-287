# MQTTSimpleClient

A custom MQTT library for interaction with a broker.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Configuration](#configuration)
  - [Logger](#logger)
  - [MQTT Client](#mqtt-client)
  - [MQTT Subscriber](#mqtt-subscriber)
- [Contributing](#contributing)


## Introduction
This library provides a simple interface to interact with an MQTT broker. It includes features like logging and configuration management.

## Features
- Singleton pattern for MQTT client
- Custom logger with rotating file handler
- XML-based configuration
- Easy to extend and customize

## Installation
To install the library, use the following command:

```sh
pip install MQTTSimpleClient
```

## Usage


### Configuration:

```ruby
<config>
    <log>
        <folder>
            <path type="string">./logs</path>
            <name type="string">app.log</name>
        </folder>
        <formatter type="string">%(asctime)s - %(name)s - %(levelname)s - %(message)s</formatter>
        <RotatingFileHandler>
            <file_size type="int">10485760</file_size>
            <backup_count type="int">5</backup_count>
        </RotatingFileHandler>
    </log>
</config>

```


### Logger
Here's how to use the custom logger:

```ruby
from MQTTSimpleClient.my_logger import Logger

logger = Logger('my_script').get_logger()
logger.info('This is an info message')
```


### MQTT Client
To create and use the MQTT client:
```ruby
from MQTTSimpleClient.mqtt_client import MqttClient

mqtt_client = MqttClient("broker_host", 1883, "client_id")
mqtt_client.connect()
mqtt_client.publish("topic", "message")
mqtt_client.disconnect()
```

### MQTT Subscriber
To create and use an MQTT subscriber:
```ruby
from MQTTSimpleClient.mqtt_client import MqttClient, MqttSubscriber

def callback_function(message):
    print(f"Message received: {message.payload.decode()}")

mqtt_client = MqttClient("broker_host", 1883, "client_id")
mqtt_client.connect()
subscriber = MqttSubscriber(mqtt_client, "topic", funzione1=callback_function)
```

## Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss what you would like to change.


