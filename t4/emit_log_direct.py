import pika

connection=pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))

channel=connection.channel()

channel.exchange_declare(exchange='direct-log',exchange_type='direct')

severty=['log','error','info']


for s in severty:
    for i in range(20):
        channel.basic_publish(exchange='direct-log',routing_key=s,body=f'sendig {i}')




print('sending')

connection.close()