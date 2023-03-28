import pika


connenction=pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))

channel=connenction.channel()

channel.queue_declare(queue='rpc-queue')

def call_back(ch,method,properties,body):
    n=int(body)
    print('processing ')

    response=n+1

    ch.basic_publish(routing_key=properties.reply_to,
                          properties=pika.BasicProperties(correlation_id=properties.correlation_id,body=str(response)))
    ch.basic_ack(delivery_tag=method.delivery_tag)




channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue='rpc-queue',on_message_callback=call_back)

print('wating for message')


channel.start_consuming()
