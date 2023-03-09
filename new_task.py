import pika
from time import sleep


connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))

channel = connection.channel()
channel.queue_declare(queue='task_queue',durable=True)


for i in range(20):
    channel.basic_publish( exchange='',
                           routing_key='task_queue',
                           body=f'new hello mehrshad {i}',
                           properties=pika.BasicProperties(
                            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
                          ))
    # sleep(2)

print('end of publish')

channel.close()