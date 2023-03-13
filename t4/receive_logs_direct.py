import pika

connection=pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))

channel=connection.channel()

channel.exchange_declare(exchange='direct-log',exchange_type='direct')

result=channel.queue_declare(queue='',exclusive=True)

queue_name=result.method.queue


severty=['log','error','info']
for s in severty:
    channel.queue_bind(exchange='direct-log',queue=queue_name,routing_key=s)


def call_back(ch,method,properties,body):
    print(f' consuming {method.routing_key}  {body}')



channel.basic_consume(queue=queue_name,on_message_callback=call_back,auto_ack=True)

print('start comsuming')

channel.start_consuming()