import time

import pika  # Импорт библиотеки pika для работы с RabbitMQ

# Устанавливаем соединение с RabbitMQ брокером
connection = pika.BlockingConnection(pika.URLParameters('amqps://gjbweibk:eL88hOkPdDTTII1I8d7mtO6nTGZscunX@cow.rmq2.cloudamqp.com/gjbweibk'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True) # Объявляем очередь с именем 'hello', если такая очередь еще не существует

print(' [*] Waiting for messages. To exit press CTRL+C')  # Выводим сообщение о начале ожидания сообщений

def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_message_callback=callback, queue='task_queue')  # Устанавливаем consumer (потребителя) для очереди
                                                             # 'hello' с указанием функции обратного вызова


channel.start_consuming()  # Начинаем прослушивание (ожидание) сообщений в очереди

