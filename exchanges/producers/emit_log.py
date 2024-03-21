import sys

import pika  # Импорт библиотеки pika для работы с RabbitMQ

# Устанавливаем соединение с RabbitMQ брокером через cloud_amqp
connection = pika.BlockingConnection(pika.URLParameters('amqps://gjbweibk:eL88hOkPdDTTII1I8d7mtO6nTGZscunX@cow.rmq2.cloudamqp.com/gjbweibk'))

# Создаем канал для обмена данными с брокером
channel = connection.channel()

#объявляем обменник с именем 'logs' и типом 'fanout'
channel.exchange_declare(exchange='logs', exchange_type='fanout')

# Выводим сообщение об отправке сообщения в консоль
message = ' '.join(sys.argv[1:]) or "info: Hello World!"

# Отправляем сообщение в обменник
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print(f" [x] Sent {message}")

connection.close()  # Закрываем соединение с брокером RabbitMQ после отправки сообщений
