import pika


connection= pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))

ch=connection.channel()

ch.exchange_declare(exchange='topic_log',exchange_type='topic')



m={'error.w.important':'important error','error.d.notimportant':'not important error'}

for k,v in m.items():
    ch.basic_publish(exchange='topic_log',routing_key=k,body=v)

print('send')
connection.close()
