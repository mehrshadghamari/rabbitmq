import pika
import uuid


class Sender():
    def __init__(self):
        self.connection=pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
        self.channel=self.connection.channel()
        result=self.channel.queue_declare(queue='',exclusive=True)
        self.qname=result.method.queue
        self.channel.basic_consume(queue=self.qname,on_message_callback=self.on_response,auto_ack=True)

    
    def on_response(self,ch,method,properties,body):
        if self.corre_id==properties.correlation_id:
            self.response=body


    def call(self,n):
        self.response=None
        self.coree_id=str(uuid.uuid4())
        self.channel.basic_publish(exchange='',routing_key='rpc-queue')


        while self.response is None :
            self.connection.process_data_events()

        return int(self.response)



send= Sender()

response=send.call(20)

print(response)