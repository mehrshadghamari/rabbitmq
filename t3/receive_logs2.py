import pika


connection= pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))

channel = connection.channel()

channel.exchange_declare(exchange='logs',exchange_type='fanout')

result=channel.queue_declare(queue='',exclusive=True)

queue_name= result.method.queue

channel.queue_bind(exchange='logs',queue=queue_name)

def call_back(ch,method,properties,body):
    print(f'receive {body}')


channel.basic_consume(queue=queue_name,on_message_callback=call_back,auto_ack=True)


print('start consuming2')

channel.start_consuming()