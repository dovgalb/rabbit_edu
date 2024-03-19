import pika

connection = pika.BlockingConnection(pika.URLParameters('amqp://admin:admin@localhost:5672'))
channel = connection.channel()

channel.queue_declare(queue='hello')
