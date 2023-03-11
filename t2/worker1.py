import pika
from time import sleep



connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))

channel=connection.channel()

channel.queue_declare(queue='task_queue',durable=True)

def call_back1(ch,method,properties,body):
    print(f'recived {body}')
    sleep(1)
    print('done')
    ch.basic_ack(delivery_tag = method.delivery_tag)
    


channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue='task_queue',on_message_callback=call_back1)

print('waiting for cosuming worker 1')

channel.start_consuming()

