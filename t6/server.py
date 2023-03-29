import pika
import time



connenction=pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))

channel=connenction.channel()

channel.queue_declare(queue='rpc_queue')

def call_back(ch,method,proper,body):
    n=int(body)
    print('processing ')
    time.sleep(5)
    response=n+1

    ch.basic_publish(exchange='',routing_key=proper.reply_to,
                          properties=pika.BasicProperties(correlation_id=proper.correlation_id,),body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)




channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue='rpc_queue',on_message_callback=call_back)

print('wating for message')


channel.start_consuming()
