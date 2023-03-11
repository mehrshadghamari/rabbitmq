import pika
from time import sleep

connection=pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
channel=connection.channel()
channel.exchange_declare(exchange='logs',exchange_type='fanout')


for i in range(20):
    channel.basic_publish(exchange='logs',routing_key='',body=f'log {i} ')
    sleep(2)

connection.close()