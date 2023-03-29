import pika
import uuid


# class Sender():
#     def __init__(self):
#         self.connection=pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
#         self.channel=self.connection.channel()
#         result=self.channel.queue_declare(queue='',exclusive=True)
#         self.qname=result.method.queue
#         self.channel.basic_consume(queue=self.qname,on_message_callback=self.on_response,auto_ack=True)

    
#     def on_response(self,ch,method,properties,body):
#         if self.corre_id==properties.correlation_id:
#             self.response=body


#     def call(self,n):
#         self.response=None
#         self.coree_id=str(uuid.uuid4())
#         self.channel.basic_publish(exchange='',routing_key='rpc-queue')


#         while self.response is None :
#             self.connection.process_data_events()

#         return int(self.response)



# send= Sender()

# response=send.call(20)

# print(response)

print('start')

class ClientSender():
    def __init__(self):
        self.connection=pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
        self.ch=self.connection.channel()
        result=self.ch.queue_declare(queue='',exclusive=True)
        self.qname=result.method.queue
        self.ch.basic_consume(queue=self.qname,on_message_callback=self.on_response,auto_ack=True)
        print('in')
        # self.ch.start_consuming()
    

    def call(self,n):
        self.response=None
        self.core_id=str(uuid.uuid4())
        self.ch.basic_publish(exchange='',routing_key='rpc_queue',
                              properties=pika.BasicProperties(reply_to=self.qname,correlation_id=self.core_id),body=str(n))

        while self.response is None :
            self.connection.process_data_events()

        return self.response

    
    def on_response(self,ch,method,properties,body):
        if self.core_id == properties.correlation_id:
            self.response=body



print('befor instance')
send= ClientSender()

print(type(send))
print('start2')
response=send.call(20)
print('start3')

print(response)