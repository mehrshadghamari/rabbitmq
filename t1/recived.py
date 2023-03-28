import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
channel = connection.channel()


def call_back(ch, method, properties, body):
    print(f'recived {body}')


channel.basic_consume(queue='hello', auto_ack=True,
                      on_message_callback=call_back)


print('waiting for cosuming')

channel.start_consuming()
