import pika


connection = pika.BlockingConnection(pika.URLParameters('amqp://admin:admin@localhost:5672'))

channel = connection.channel()

channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')

for i in range(100):
    print("[x] Sent 'Hello World!'")

connection.close()


# import pika
#
# params = pika.URLParameters('amqps://gjbweibk:eL88hOkPdDTTII1I8d7mtO6nTGZscunX@cow.rmq2.cloudamqp.com/gjbweibk')
# connection = pika.BlockingConnection(params)
#
# channel = connection.channel()
#
# channel.queue_declare(queue='hello')
# channel.basic_publish(exchange='',
#                       routing_key='hello',
#                       body='Hello World!')
#
# print(" [x] Sent 'Hello World!'")
#
# connection.close()
