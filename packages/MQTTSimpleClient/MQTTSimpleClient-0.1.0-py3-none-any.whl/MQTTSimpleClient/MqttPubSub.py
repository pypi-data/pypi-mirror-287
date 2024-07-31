# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 14:51:40 2023

@author: sPK-Server
"""

import paho.mqtt.client as mqtt
from time import sleep
from .my_logger import Logger

# Create a logger
logger = Logger(__name__.split(".")[-1]).get_logger()

import threading
from typing import Optional


class MqttClient:
    _instances = {}
    _lock = threading.Lock()

    def __new__(cls, broker_host: str, broker_port: int, client_id: str,
                username: Optional[str] = None, password: Optional[str] = None, **kwargs):
        with cls._lock:
            if client_id not in cls._instances:
                instance = super().__new__(cls)
                cls._instances[client_id] = instance
            return cls._instances[client_id]

    def __init__(self, broker_host: str, broker_port: int, client_id: str,
                 username: Optional[str] = None, password: Optional[str] = None, **kwargs):
        if not hasattr(self, 'initialized'):
            self.__broker_host = broker_host
            self.__broker_port = broker_port
            self.__client_id = client_id
            self.__username = username
            self.__password = password
            self.__client = mqtt.Client(client_id=client_id)
            self.__connected: bool = False
            self.__topic = ""
            self.__qos = 0

            # Connect MQTT event handlers
            self.__client.on_connect = self.__on_connect
            self.__client.on_publish = self.__on_publish
            self.__client.on_disconnect = self.__on_disconnect

            self.initialized = True
            logger.info(f"Module initialized")

    def __on_connect(self, client, userdata, flags, rc) -> None:
        if rc == 0:
            self.__connected = True
            logger.info(f"Client <{self.__client_id}> - Connected to the MQTT broker {self.__broker_host}")
        else:
            logger.error(f"Client <{self.__client_id}> - MQTT broker connection failed due to: " + str(rc))

    def __on_disconnect(self, client, userdata, rc):
        logger.info(f"Client <{self.__client_id}> - Disconnected from MQTT broker {self.__broker_host} cod. {rc}")

    def __on_publish(self, client, userdata, mid) -> None:
        logger.info(f"Client <{self.__client_id}> - Message successfully published Mid: <{str(mid)}> topic <{self.__topic}> qos <{self.__qos}>")

    def connect(self, asyncronous=False) -> None:
        logger.info(f"Client <{self.__client_id}> - Test Connection MQTT broker <{self.__broker_host}>")
        if self.__username and self.__password:
            self.__client.username_pw_set(self.__username, self.__password)
        if asyncronous:
            self.__client.connect_async(self.__broker_host, self.__broker_port, 60)
        else:
            self.__client.connect(self.__broker_host, self.__broker_port, 60)
        sleep(0.1)

    def publish(self, topic: str, message: str, qos=0, retain=False) -> None:
        self.__topic = topic
        self.__qos = qos
        try:
            self.__client.publish(topic, message, qos, retain)
        except Exception as e:
            logger.error(f"Client <{self.__client_id}> - not connected to the MQTT broker <{self.__broker_host}> -> "
                         f"Unable to publish message: {e}")
        sleep(0.1)

    def run(self):
        self.__client.loop_start()
        logger.info(f"Client <{self.__client_id}> - Client Loop Start")

    def run_forever(self):
        logger.info(f"Client <{self.__client_id}> - Client Loop_Forever Start")
        self.__client.loop_forever()

    def disconnect(self) -> None:
        self.__client.disconnect()
        self.__client.loop_stop()
        self.__connected = False

    @property
    def client(self):
        return self.__client

    @property
    def connected(self) -> bool:
        return self.__connected

    @property
    def broker_host(self):
        return self.__broker_host

    @property
    def client_id(self):
        return self.__client_id


class MqttSubscriber:
    __instances = {}

    def __init__(self, client: MqttClient, topic: str, qos: int = 0, **callback):

        self.__client = client
        self.__topic = topic
        self.__qos = qos

        # Connect MQTT event handlers
        self.__client.client.on_connect = self.__on_connect

        # Load subscription callback function
        self.__callback = {}
        for key, value in callback.items():
            if callable(value):
                self.__callback[key] = value
            else:
                logger.warning(f"Il valore passato per '{key}' non è una funzione. Verrà ignorato.")

        # self.__subscribe()
        MqttSubscriber.__instances[topic] = self

    def __on_connect(self, client, userdata, flags, rc) -> None:
        if rc == 0:
            self.__connected = True
            MqttSubscriber.__subscribe_all()
            logger.info(f"Client <{self.__client.client_id}> - connected to the MQTT broker {self.__client.broker_host}")
        else:
            logger.error(f"Client <{self.__client.client_id}> - MQTT broker connection failed due to: " + str(rc))

    def __on_message(self, client, userdata, message):
        logger.info(f"Client <{self.__client.client_id}> - message received on topic {message.topic}:"
                    f" {message.payload.decode()[:40]} ... ")
        self.__message = message

        for k, func in self.__callback.items():
            sleep(0.1)
            try:
                func(self.__message)
                sleep(0.1)
            except TypeError as e:
                logger.error(f"Client <{self.__client.client_id}> - Error in __on_message() callback: {str(e)}")

    def __subscribe(self) -> None:

        logger.info(f"Client <{self.__client.client_id}> - Test subscription: topic <{self.__topic}>")

        self.__client.client.subscribe(self.__topic, self.__qos)
        self.__client.client.message_callback_add(self.__topic, self.__on_message)
        logger.info(f"Client <{self.__client.client_id}> - Subscription established on topic '{self.__topic}':"
                    f" QoS <{str(self.__qos)}>, callback <{list(self.__callback.keys())}>")
        sleep(0.1)

    def unsubscribe(self) -> None:
        if self.__topic:

            self.__client.client.unsubscribe(self.__topic)
            logger.info(f"Client <{self.__client.client_id}> - Subscription cancelled to topic " + self.__topic)
            self.__topic = ''
        else:
            logger.error("No active subscription")

    @classmethod
    def __subscribe_all(cls):
        for instance in cls.__instances.values():
            instance.__subscribe()

    @classmethod
    def unsubscribe_all(cls):
        for instance in cls.__instances.values():
            instance.unsubscribe()


if __name__ == "__main__":

    def func1(message, casa):
        print(f"Funzione 1: {message.payload.decode()}")


    def func2(message):
        print(f"Funzione 2: {message.payload.decode()}")


    def func3(message):
        print(f"Funzione 3: {message.payload.decode()}")


    mqtt_client = MqttClient("10.7.68.9", 1883, f"{__name__}_test")
    mqtt_client.connect()
    mqtt_client.run()
    if mqtt_client.connected:
        # Pubblica un messaggio
        mqtt_client.publish("Postman",
                            '{"InfluxDB": {"databases": "manz_dbs, manz_calculated_db", "start": '
                            '"2023-06-01T00:00:00Z", "stop": "2023-07-01T00:00:00Z"}}')

    # Test di connessione
    if mqtt_client.connected:
        # Sottoscrivi a un topic
        sub1 = MqttSubscriber(mqtt_client, "Test")

        sub2 = MqttSubscriber(mqtt_client, "Postman", funzione1=func1)

        sub3 = MqttSubscriber(mqtt_client, "Funzione",
                              funzione2=func2, funzione3=func3, funzione4=4)

    sleep(0.1)
    input("Premi Enter per terminare la sottoscrizione...")
    sub1.unsubscribe()
    sub2.unsubscribe()
    sub3.unsubscribe()

    sleep(0.1)
    input("Premi Enter per disconnettersi...")
    mqtt_client.disconnect()
