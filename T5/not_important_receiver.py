import pika


connection= pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))

ch=connection.channel()

ch.exchange_declare(exchange='topic_log',exchange_type='topic')

result=ch.queue_declare(queue='',exclusive=True)

qname=result.method.queue


binding_key='#.notimportant'

ch.queue_bind(exchange='topic_log',queue=qname,routing_key=binding_key)

print('wating')

def callback(ch,method,properties,body):
    print(body)


ch.basic_consume(queue=qname,auto_ack=True,on_message_callback=callback)
ch.start_consuming()