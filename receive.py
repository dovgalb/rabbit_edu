import pika  # Импорт библиотеки pika для работы с RabbitMQ

# Устанавливаем соединение с RabbitMQ брокером
connection = pika.BlockingConnection(pika.URLParameters('amqp://admin:admin@localhost:5672'))
channel = connection.channel()

channel.queue_declare(queue='hello')  # Объявляем очередь с именем 'hello', если такая очередь еще не существует

print(' [*] Waiting for messages. To exit press CTRL+C')  # Выводим сообщение о начале ожидания сообщений


def callback(ch, method, properties, body):
    """ Функция обратного вызова, которая будет вызываться при получении сообщения"""
    print(" [x] Received %r" % (body,))


channel.basic_consume(on_message_callback=callback, queue='hello', auto_ack=True)  # Устанавливаем consumer (потребителя) для очереди
                                                             # 'hello' с указанием функции обратного вызова


channel.start_consuming()  # Начинаем прослушивание (ожидание) сообщений в очереди

