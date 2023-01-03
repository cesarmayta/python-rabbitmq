import pika

import os

from dotenv import load_dotenv


class Conexion:
"""Esta clase encapsulara la conexión a RabbitMQ"""
    enlace = None
    canal = None
    
    def __init__(self,dotenv_path=".env"):
        load_dotenv(dotenv_path=dotenv_path)
        
        parameters= pika.URLParameters('amqp://{}:{}@localhost:5672/clubprog'.format(os.environ.get('TEST_USER'),os.environ.get('TEST_PASS')))

        self.enlace = pika.BlockingConnection( parameters )

        self.canal = self.enlace.channel()

        self.canal.queue_declare(queue='platziq')