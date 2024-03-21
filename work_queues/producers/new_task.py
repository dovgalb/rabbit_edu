import sys

import pika  # Импорт библиотеки pika для работы с RabbitMQ

# Устанавливаем соединение с RabbitMQ брокером
connection = pika.BlockingConnection(pika.URLParameters('amqps://gjbweibk:eL88hOkPdDTTII1I8d7mtO6nTGZscunX@cow.rmq2.cloudamqp.com/gjbweibk'))

# Создаем канал для обмена данными с брокером
channel = connection.channel()

# Объявляем очередь с именем 'hello', если такая очередь еще не существует
channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode = 2,
                      ))
print(f" [x] Sent {message}")

connection.close()  # Закрываем соединение с брокером RabbitMQ после отправки сообщений
